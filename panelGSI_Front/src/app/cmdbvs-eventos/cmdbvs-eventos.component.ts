import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-cmdbvs-eventos',
  templateUrl: './cmdbvs-eventos.component.html',
  styleUrl: './cmdbvs-eventos.component.scss'
})
export class CMDBvsEventosComponent {

  dataCMDBvsEve: any[] = [];
  totalallazosCMDBvsEve: number = 0;
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVCMDB'];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataCMDB().subscribe(dataCMDBvsEve => {
      this.dataCMDBvsEve = dataCMDBvsEve;
      console.log(this.dataCMDBvsEve);
      this.totalallazosCMDBvsEve = this.dataCMDBvsEve.length;
      console.log(this.totalallazosCMDBvsEve);
    })
  }

}
