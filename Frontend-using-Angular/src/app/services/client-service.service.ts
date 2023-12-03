import { Injectable } from '@angular/core';
import {Client} from "../modules/Client";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class ClientServiceService {
  private apiServerUrl = environment.apiBaseUrl;


  constructor(private http: HttpClient) {}
  public addClient(client: Client): Observable<Client> {
    return this.http.post<Client>(`${this.apiServerUrl}/clients`, client);
  }

}
