import { Component, OnInit } from '@angular/core';
import {AbonementServiceService} from "../services/abonement-service.service";
import {HttpErrorResponse} from "@angular/common/http";
import {Infos} from "../modules/Infos";
import {Router} from "@angular/router";

@Component({
  selector: 'app-list-all-abonement',
  templateUrl: './list-all-abonement.component.html',
  styleUrls: ['./list-all-abonement.component.css']
})
export class ListAllAbonementComponent implements OnInit {

  infos ! : Array<Infos>;


  constructor(private infoService : AbonementServiceService,private abonnementService:AbonementServiceService,private router:Router) { }

  ngOnInit(): void {
    this.handelGetAllinfo();
  }

  handelGetAllinfo(){
    this.infoService.getinfo().subscribe({

      next:(data)=>{
        this.infos = data;
      },error: (error: HttpErrorResponse) => {
        console.error(error);
        alert("Error get all data ");
      }
    })
  }


  // onDeleteButtonClick(info: Infos) {
  //   this.router.navigateByUrl(`/edit/${info.matricule}`);
  //
  // }

  handelRaport(info: Infos) {
    this.router.navigateByUrl(`/ListRaportClient/${info.matricule}`);
  }
}
