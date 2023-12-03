import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ErorrServiceService} from "../services/erorr-service.service";
import {ActivatedRoute} from "@angular/router";
import {Infos} from "../modules/Infos";
import {AbonementServiceService} from "../services/abonement-service.service";

@Component({
  selector: 'app-edit-abonement',
  templateUrl: './edit-abonement.component.html',
  styleUrls: ['./edit-abonement.component.css']
})
export class EditAbonementComponent implements OnInit {
  infoFormGroup! : FormGroup;
  infoMatricule!:string;
  info!:Infos;

  constructor(private fb :FormBuilder, public ErorreService :ErorrServiceService,private route : ActivatedRoute,private infosService:AbonementServiceService) {
    this.infoMatricule = this.route.snapshot.params['matricule'];
  }

  ngOnInit(): void {
    this.infosService.getinfoMatricule(this.infoMatricule).subscribe({
      next : (data)=>{
        this.info=data;
      }
    })
    this.infoFormGroup=this.fb.group({
      sold : this.fb.control(this.info.sold,[Validators.required]),
      // matricule : this.fb.control(this.info.matricule,Validators.required),
      // model : this.fb.control(this.info.model,Validators.required),
      // fullname : this.fb.control(this.info.fullname,[Validators.required]),
      // email : this.fb.control(this.info.email,[Validators.required,Validators.email]),
      // phone_number : this.fb.control(this.info.phone_number,[Validators.required,Validators.pattern(/^[0-9]{10}$/)]),
      // cin : this.fb.control(this.info.cin,[Validators.required]),
      // age : this.fb.control(this.info.age,[Validators.required, Validators.min(18), Validators.max(100)]),
    })
  }
  handelEditSold() {

  }
}
