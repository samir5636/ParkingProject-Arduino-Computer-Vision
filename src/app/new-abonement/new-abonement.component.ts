import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ErorrServiceService} from "../services/erorr-service.service";
import {Car} from "../modules/Car";
import {HttpErrorResponse} from "@angular/common/http";
import {AbonementServiceService} from "../services/abonement-service.service";
import {Abonement} from "../modules/Abonement";

@Component({
  selector: 'app-new-abonement',
  templateUrl: './new-abonement.component.html',
  styleUrls: ['./new-abonement.component.css']
})
export class NewAbonementComponent implements OnInit {

  abonementFormGroup! : FormGroup;

  constructor(private fb :FormBuilder, public abonementErorreService :ErorrServiceService,private abonementService : AbonementServiceService) { }


  ngOnInit(): void {
    this.abonementFormGroup=this.fb.group({
      matricule : this.fb.control(null,[Validators.required]),
      sold : this.fb.control(null,[Validators.required]),
    })
  }

  handelAbonement() {
      let newAbonment = this.abonementFormGroup.value;
      this.abonementService.addAbonement(newAbonment).subscribe({
        next: (response:Abonement) => {
          console.log(response);
          alert("Abonement added successfully");
          this.abonementFormGroup.reset();
        },
        error: (error: HttpErrorResponse) => {
          console.error(error);
          alert("Error adding Abonement");
          this.abonementFormGroup.reset();
        }
      });
    }
}
