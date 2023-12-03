import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ErorrServiceService} from "../services/erorr-service.service";

@Component({
  selector: 'app-refrech-abonement',
  templateUrl: './refrech-abonement.component.html',
  styleUrls: ['./refrech-abonement.component.css']
})
export class RefrechAbonementComponent implements OnInit {

  refreshFormGroup!:FormGroup;

  constructor(private fb:FormBuilder, public refreshserviceErorre:ErorrServiceService) { }


  ngOnInit(): void {
    this.refreshFormGroup=this.fb.group({
      matricule : this.fb.control(null,[Validators.required]),
      solde : this.fb.control(null,[Validators.required]),
    })
  }

  handelRefresh() {

  }
}
