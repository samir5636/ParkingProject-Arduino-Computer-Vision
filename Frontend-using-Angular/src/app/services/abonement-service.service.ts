import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Abonement} from "../modules/Abonement";
import {Infos} from "../modules/Infos";
import {Raport} from "../modules/Raport";

@Injectable({
  providedIn: 'root'
})
export class AbonementServiceService {
  private apiServerUrl = environment.apiBaseUrl;
  constructor(private http: HttpClient) { }
  public addAbonement(abonement: Abonement): Observable<Abonement> {
    return this.http.post<Abonement>(`${this.apiServerUrl}/abonements/add`, abonement);
  }

  public getinfo(): Observable<Array<Infos>> {
    return this.http.get<Array<Infos>>(`${this.apiServerUrl}/info`);
  }
  public getinfoMatricule(matriculeInfo:string): Observable<Infos> {
    return this.http.get<Infos>(`${this.apiServerUrl}/info/${matriculeInfo}`);
  }
  // public updateAbonnement(abonnementId: number, sold: number): Observable<number> {
  //   return this.http.put<number>(`${this.apiServerUrl}/abonnements/${abonnementId}`, { sold });
  // }

    public getRaport(matricule: string): Observable<Array<Raport>> {
        return this.http.get<Array<Raport>>(`${this.apiServerUrl}/rapport/${matricule}`);
    }

}
