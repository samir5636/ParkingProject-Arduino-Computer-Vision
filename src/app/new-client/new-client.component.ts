import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

import {ErorrServiceService} from "../services/erorr-service.service";
import {ClientServiceService} from "../services/client-service.service";
import {Client} from "../modules/Client";
import {HttpErrorResponse} from "@angular/common/http";


@Component({
  selector: 'app-new-client',
  templateUrl: './new-client.component.html',
  styleUrls: ['./new-client.component.css']
})
export class NewClientComponent implements OnInit {

  clientFormGroup!: FormGroup;
  public client! :Client[];

  constructor(private fb: FormBuilder, public clientServiceErorre:ErorrServiceService,private clientService:ClientServiceService) { }

  ngOnInit(): void {
    this.clientFormGroup=this.fb.group({
      fullname : this.fb.control(null,[Validators.required]),
      email : this.fb.control(null,[Validators.required,Validators.email]),
      phone_number : this.fb.control(null,[Validators.required,Validators.pattern(/^[0-9]{10}$/)]),
      cin : this.fb.control(null,[Validators.required]),
      age : this.fb.control(null,[Validators.required, Validators.min(18), Validators.max(100)]),
    })
  }

  handelClient() {
    let newClient = this.clientFormGroup.value;
    this.clientService.addClient(newClient).subscribe({
      next: (response: Client) => {
        console.log(response);
        alert("Client added successfully");
        this.clientFormGroup.reset();
      },
      error: (error: HttpErrorResponse) => {
        console.error(error);
        alert("Error adding client");
        this.clientFormGroup.reset();
      }
    });
  }
}
