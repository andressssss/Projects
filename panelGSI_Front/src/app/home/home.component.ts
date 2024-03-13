import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';
import { CMDBvsEventosComponent } from '../cmdbvs-eventos/cmdbvs-eventos.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})

export class HomeComponent {

  dataCMDBvsEve: any[] = [];
  dataLBvsEve: any[] = [];
  cruceSelec: string = "";
  totalallazos: number = 0;
  totalallazosLBvsEve: number = 0;
  totalallazosCMDBvsEve: number = 0;
  totalallazosEVENTOS: number = 0;
  estadoartefacto: boolean = false;
  lineabaseVSeventosSHOW:boolean = false;
  CMDBVSeventosSHOW:boolean = false;

  constructor(private apiService: ApiService,
              private cmdbvseveComponent: CMDBvsEventosComponent){

  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataCMDB().subscribe(dataCMDBvsEve => {
      this.dataCMDBvsEve = dataCMDBvsEve;
      this.totalallazosCMDBvsEve = this.dataCMDBvsEve.length;
      this.totalallazosEVENTOS += this.dataCMDBvsEve.length
      console.log(this.totalallazosCMDBvsEve);
    })
    this.apiService.getData().subscribe(dataLBvsEve => {
      this.dataLBvsEve = dataLBvsEve;
      console.log(this.dataLBvsEve);
      this.totalallazosLBvsEve = this.dataLBvsEve.length;
      this.totalallazosEVENTOS += this.dataLBvsEve.length
      console.log(this.totalallazosLBvsEve);
    })

    this.totalallazosEVENTOS = this.totalallazosCMDBvsEve+this.totalallazosLBvsEve
    console.log(this.totalallazosEVENTOS);
  }

  onPulse(value :string){
    console.log(value)

    switch (value){
      case('EventosvsLB'):
        this.cruceSelec = "Lineabase vs Eventos";
        this.lineabaseVSeventosSHOW = true;
        this.CMDBVSeventosSHOW = false;
      break

      case("EventosvsCMDB"):
        this.cruceSelec = "CMDB vs Eventos";
        this.CMDBVSeventosSHOW = true;
        this.lineabaseVSeventosSHOW = false;
      break
    }
    }

    estadoartEventos(){
      var estadoart = 0;
      switch (this.totalallazosLBvsEve){
        case 0-30:
          estadoart = 3
        break
        case 30-100:
          estadoart = 2
        break
        case 100-100000000:
          estadoart = 1
        break
      }
      return estadoart;
    }
}
