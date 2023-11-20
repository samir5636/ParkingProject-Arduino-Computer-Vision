import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {NewClientComponent} from "./new-client/new-client.component";
import {NewAbonementComponent} from "./new-abonement/new-abonement.component";
import {ListAllAbonementComponent} from "./list-all-abonement/list-all-abonement.component";
import {ListCarInParkingComponent} from "./list-car-in-parking/list-car-in-parking.component";
import {NewCarComponent} from "./new-car/new-car.component";
import {EditAbonementComponent} from "./edit-abonement/edit-abonement.component";
import {RefrechAbonementComponent} from "./refrech-abonement/refrech-abonement.component";
const routes: Routes = [
  {path: "Client" ,component: NewClientComponent },
  {path: "Abonement" ,component: NewAbonementComponent },
  {path: "Car" ,component: NewCarComponent },
  {path: "ListAbonement" ,component: ListAllAbonementComponent },
  {path: "edit" ,component: EditAbonementComponent },
  {path: "refresh" ,component: RefrechAbonementComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
