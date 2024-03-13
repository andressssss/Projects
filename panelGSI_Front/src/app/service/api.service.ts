import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private urlApiLBvsEve = 'http://127.0.0.1:8000/api/LineabasevsEventos';
  private urlApiCMDBvEve = 'http://127.0.0.1:8000/api/CMDBvseventos';

  constructor(private http: HttpClient) {

  }

  public getData(): Observable<any>{
    return this.http.get<any>(this.urlApiLBvsEve);
  }

  public getDataCMDB(): Observable<any>{
    return this.http.get<any>(this.urlApiCMDBvEve);
  }

}
