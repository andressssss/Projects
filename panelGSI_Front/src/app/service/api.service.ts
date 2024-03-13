import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private urlApiLBvsEve = 'http://127.0.0.1:8000/api/LineabasevsEventos';
  private urlApiCMDBvEve = 'http://127.0.0.1:8000/api/CMDBvseventos';
  private urlApiCMDBvsLB = 'http://127.0.0.1:8000/api/CMDBvsLineabase';
  private urlApiEvevsLB = 'http://127.0.0.1:8000/api/EventosvsLineabase';
  private urlApiLBvsCMDB = 'http://127.0.0.1:8000/api/LineabasevsCMDB';
  private urlApiEvevsCMDB = 'http://127.0.0.1:8000/api/EventosvsCMDB/';

  constructor(private http: HttpClient) {

  }

  public getData(): Observable<any>{
    return this.http.get<any>(this.urlApiLBvsEve);
  }

  public getDataCMDB(): Observable<any>{
    return this.http.get<any>(this.urlApiCMDBvEve);
  }

  public getDataCMDBvsLB(): Observable<any>{
    return this.http.get<any>(this.urlApiCMDBvsLB);
  }

  public getDataEvevsLB(): Observable<any>{
    return this.http.get<any>(this.urlApiEvevsLB);
  }

  public getDataLBvsCMDB(): Observable<any>{
    return this.http.get<any>(this.urlApiLBvsCMDB);
  }

  public getDataEvevsCMDB(): Observable<any>{
    return this.http.get<any>(this.urlApiEvevsCMDB);
  }
}
