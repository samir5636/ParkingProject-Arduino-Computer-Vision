import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ErorrServiceService} from "../services/erorr-service.service";
import {Client} from "../modules/Client";
import {HttpErrorResponse} from "@angular/common/http";
import {CarServiceService} from "../services/car-service.service";
import {Car} from "../modules/Car";

@Component({
  selector: 'app-new-car',
  templateUrl: './new-car.component.html',
  styleUrls: ['./new-car.component.css']
})
export class NewCarComponent implements OnInit {

  carFormGroup! : FormGroup;
  constructor(private fb :FormBuilder , public carServiceErorre :ErorrServiceService, private carServise:CarServiceService) { }

  ngOnInit(): void {
    this.carFormGroup=this.fb.group({
      cin : this.fb.control(null,Validators.required),
      matricule : this.fb.control(null,Validators.required),
      model : this.fb.control(null,Validators.required),
    })
  }

  handelCar() {
    let newcar = this.carFormGroup.value;
    this.carServise.addCar(newcar).subscribe({
      next: (response:Car) => {
        console.log(response);
        alert("Car added successfully");
        this.carFormGroup.reset();
      },
      error: (error: HttpErrorResponse) => {
        console.error(error);
        alert("Error adding car");
        this.carFormGroup.reset();
      }
    });
  }
}
