import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Car} from "../modules/Car";
import { NumbrCarTotal} from "../modules/NmbrCarTotalAndInParking";
import {NumberCarIN} from "../modules/Total";

@Injectable({
  providedIn: 'root'
})
export class CarServiceService {
  private apiServerUrl = environment.apiBaseUrl;

  constructor(private http: HttpClient) { }

  public addCar(car: Car): Observable<Car> {
    return this.http.post<Car>(`${this.apiServerUrl}/cars/add`, car);

  }
  public nbrTotalCar(): Observable<NumbrCarTotal> {
    return this.http.get<NumbrCarTotal>(`${this.apiServerUrl}/cars/nbr`);
  }
  public nbrCarInparking(): Observable<NumberCarIN> {
    return this.http.get<NumberCarIN>(`${this.apiServerUrl}/cars/nbrinparking`);
  }

}
