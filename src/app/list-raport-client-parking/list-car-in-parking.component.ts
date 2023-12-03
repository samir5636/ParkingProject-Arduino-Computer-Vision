import { Component, OnInit } from '@angular/core';
import {AbonementServiceService} from "../services/abonement-service.service";
import {Raport} from "../modules/Raport";
import {HttpErrorResponse} from "@angular/common/http";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-list-car-in-parking',
  templateUrl: './list-car-in-parking.component.html',
  styleUrls: ['./list-car-in-parking.component.css']
})
export class ListRaportClientComponent implements OnInit {

  raport ! : Array<Raport>;
  matricule!:string;
  constructor(private raportService :AbonementServiceService,private route : ActivatedRoute) {
      this.matricule = this.route.snapshot.params['matricule'];
  }

  ngOnInit(): void {
      this.handelGetRaport();
  }
    handelGetRaport() {
        this.raportService.getRaport(this.matricule).subscribe({
            next: (data) => {
                this.raport = data;
            },
            error: (error: HttpErrorResponse) => {
                console.error(error);
                alert('Error getting raport');
            },
        });
    }


}
