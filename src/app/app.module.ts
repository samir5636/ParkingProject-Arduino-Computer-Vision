import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NavBarComponent } from './nav-bar/nav-bar.component';
import { ListCarInParkingComponent } from './list-car-in-parking/list-car-in-parking.component';
import { NewClientComponent } from './new-client/new-client.component';
import { NewAbonementComponent } from './new-abonement/new-abonement.component';
import { NewCarComponent } from './new-car/new-car.component';
import { StatisticComponent } from './statistic/statistic.component';
import { ListAllAbonementComponent } from './list-all-abonement/list-all-abonement.component';
import { EditAbonementComponent } from './edit-abonement/edit-abonement.component';
import { RefrechAbonementComponent } from './refrech-abonement/refrech-abonement.component';
import {ReactiveFormsModule} from "@angular/forms";
import { ChartModule } from 'angular-highcharts';

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    ListCarInParkingComponent,
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
    ChartModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
