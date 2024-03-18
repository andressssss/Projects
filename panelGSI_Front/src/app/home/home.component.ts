import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})

export class HomeComponent {

  dataCMDBvsEve: any[] = [];
  dataLBvsEve: any[] = [];
  dataLBvsCMDB: any[] = [];
  dataEvevsCMDB: any[] = [];
  dataCMDBvsLB: any[] = [];
  dataEvevsLB: any[] = [];

  cruceSelec: string = "";

  totalhallazos: number = 0;

  totalhallazosLBvsEve: number = 0;
  totalhallazosCMDBvsEve: number = 0;
  totalhallazosEVENTOS: number = 0;

  totalhallazosLBvsCMDB: number = 0;
  totalhallazosEvevsCMDB: number = 0;
  totalhallazosCMDB: number = 0;

  totalhallazosEvevsLB: number = 0;
  totalhallazosCMDBvsLB: number = 0;
  totalhallazosLB: number = 0;

  estadoartefacto: boolean = false;

  lineabaseVSeventosSHOW:boolean = false;
  CMDBVSeventosSHOW:boolean = false;
  lineabasevsCMDBShow:boolean = false;
  eventosvsCMDBShow:boolean = false;
  CMDBvsLineabaseShow:boolean = false;
  eventosvsLineabaseShow:boolean = false;

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataCMDB().subscribe(dataCMDBvsEve => {
      this.dataCMDBvsEve = dataCMDBvsEve;
      this.totalhallazosCMDBvsEve = this.dataCMDBvsEve.length;
      this.totalhallazosEVENTOS += this.dataCMDBvsEve.length
      console.log(this.totalhallazosCMDBvsEve);
    })
    this.apiService.getData().subscribe(dataLBvsEve => {
      this.dataLBvsEve = dataLBvsEve;
      console.log(this.dataLBvsEve);
      this.totalhallazosLBvsEve = this.dataLBvsEve.length;
      this.totalhallazosEVENTOS += this.dataLBvsEve.length
      console.log(this.totalhallazosLBvsEve);
    })
    this.apiService.getDataLBvsCMDB().subscribe(dataLBvsCMDB => {
      this.dataLBvsCMDB = dataLBvsCMDB;
      console.log(this.dataLBvsCMDB);
      this.totalhallazosLBvsCMDB = this.dataLBvsCMDB.length;
      this.totalhallazosCMDB += this.dataLBvsCMDB.length
      console.log(this.totalhallazosLBvsCMDB);
    })
    this.apiService.getDataEvevsCMDB().subscribe(dataEvevsCMDB => {
      this.dataEvevsCMDB = dataEvevsCMDB;
      console.log(this.dataEvevsCMDB);
      this.totalhallazosEvevsCMDB = this.dataEvevsCMDB.length;
      this.totalhallazosCMDB += this.dataEvevsCMDB.length
      console.log(this.totalhallazosEvevsCMDB);
    })
    this.apiService.getDataCMDBvsLB().subscribe(dataCMDBvsLB => {
      this.dataCMDBvsLB = dataCMDBvsLB;
      console.log(this.dataCMDBvsLB);
      this.totalhallazosCMDBvsLB = this.dataCMDBvsLB.length;
      this.totalhallazosLB += this.dataCMDBvsLB.length
      console.log(this.totalhallazosCMDBvsLB);
    })
    this.apiService.getDataEvevsLB().subscribe(dataEvevsLB => {
      this.dataEvevsLB = dataEvevsLB;
      console.log(this.dataEvevsLB);
      this.totalhallazosEvevsLB = this.dataEvevsLB.length;
      this.totalhallazosLB += this.dataEvevsLB.length
      console.log(this.totalhallazosEvevsLB);
    })

    console.log(this.totalhallazosEVENTOS);
    console.log(this.totalhallazosCMDB);
    console.log(this.totalhallazosLB);
  }

  onPulse(value :string){
    console.log(value)

    switch (value){
      case('EventosvsLB'):
        this.cruceSelec = "Lineabase vs Eventos";
        this.lineabaseVSeventosSHOW = true;
        this.CMDBVSeventosSHOW = false;
        this.lineabasevsCMDBShow = false;
        this.eventosvsCMDBShow = false;
        this.CMDBvsLineabaseShow = false;
        this.eventosvsLineabaseShow = false;
      break

      case("EventosvsCMDB"):
        this.cruceSelec = "CMDB vs Eventos";
        this.CMDBVSeventosSHOW = true;
        this.lineabaseVSeventosSHOW = false;
        this.lineabasevsCMDBShow = false;
        this.eventosvsCMDBShow = false;
        this.CMDBvsLineabaseShow = false;
        this.eventosvsLineabaseShow = false;
      break

      case("CMDBvsLB"):
        this.cruceSelec = "Lineabase vs CMDB";
        this.CMDBVSeventosSHOW = false;
        this.lineabaseVSeventosSHOW = false;
        this.lineabasevsCMDBShow = true;
        this.eventosvsCMDBShow = false;
        this.CMDBvsLineabaseShow = false;
        this.eventosvsLineabaseShow = false;
      break

      case("CMDBvsEventos"):
        this.cruceSelec = "Eventos vs CMDB";
        this.CMDBVSeventosSHOW = false;
        this.lineabaseVSeventosSHOW = false;
        this.lineabasevsCMDBShow = false;
        this.eventosvsCMDBShow = true;
        this.CMDBvsLineabaseShow = false;
        this.eventosvsLineabaseShow = false;
      break

      case("LBvsCMDB"):
        this.cruceSelec = "CMDB vs Lineabase";
        this.CMDBVSeventosSHOW = false;
        this.lineabaseVSeventosSHOW = false;
        this.lineabasevsCMDBShow = false;
        this.eventosvsCMDBShow = false;
        this.CMDBvsLineabaseShow = true;
        this.eventosvsLineabaseShow = false;
      break

      case("LBvsEventos"):
        this.cruceSelec = "Eventos vs Lineabase";
        this.CMDBVSeventosSHOW = false;
        this.lineabaseVSeventosSHOW = false;
        this.lineabasevsCMDBShow = false;
        this.eventosvsCMDBShow = false;
        this.CMDBvsLineabaseShow = false;
        this.eventosvsLineabaseShow = true;
      break

    }
    }

    estadoartEventos(){
      var estadoart = 0;
      var x = this.totalhallazosEVENTOS;
      switch (true){
        case (x < 30):
          estadoart = 2
        break
        case (x >= 30 && x < 100):
          estadoart = 1
        break
        case (x >= 100 && x < 1000000):
          estadoart = 0
        break
      }
      return estadoart;
    }

    estadoartCMDB(){
      var estadoart = 0;
      var x = this.totalhallazosCMDB;
      switch (true){
        case (x < 30):
          estadoart = 2
        break
        case (x >= 30 && x < 100):
          estadoart = 1
        break
        case (x >= 100 && x < 1000000):
          estadoart = 0
        break
      }
      return estadoart;
    }

    estadoartLineabase(){
      var estadoart = 0;
      var x = this.totalhallazosLB;
      switch (true){
        case (x < 30):
          estadoart = 2
        break
        case (x >= 30 && x < 100):
          estadoart = 1
        break
        case (x >= 100 && x < 1000000):
          estadoart = 0
        break
      }
      return estadoart;
    }
}
