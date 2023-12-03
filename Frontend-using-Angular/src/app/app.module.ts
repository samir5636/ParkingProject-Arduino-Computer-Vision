import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NavBarComponent } from './nav-bar/nav-bar.component';
import { ListRaportClientComponent } from './list-raport-client-parking/list-car-in-parking.component';
import { NewClientComponent } from './new-client/new-client.component';
import { NewAbonementComponent } from './new-abonement/new-abonement.component';
import { NewCarComponent } from './new-car/new-car.component';
import { StatisticComponent } from './statistic/statistic.component';
import { ListAllAbonementComponent } from './list-all-abonement/list-all-abonement.component';
import { EditAbonementComponent } from './edit-abonement/edit-abonement.component';
import { RefrechAbonementComponent } from './refrech-abonement/refrech-abonement.component';
import {ReactiveFormsModule} from "@angular/forms";
import { ChartModule } from 'angular-highcharts';
import {HttpClientModule} from "@angular/common/http";
import {ClientServiceService} from "./services/client-service.service";
import {CarServiceService} from "./services/car-service.service";
import {AbonementServiceService} from "./services/abonement-service.service";
import {ErorrServiceService} from "./services/erorr-service.service";

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    ListRaportClientComponent,
    NewClientComponent,
    NewAbonementComponent,
    NewCarComponent,
    StatisticComponent,
    ListAllAbonementComponent,
    EditAbonementComponent,
    RefrechAbonementComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    ChartModule
  ],
  providers: [ClientServiceService,
  CarServiceService,
  AbonementServiceService,
    ErorrServiceService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
