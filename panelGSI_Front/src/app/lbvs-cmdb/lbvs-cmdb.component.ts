import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';
export interface resultado{
  aplicacion : string;
  nombreSVLB: string;
}

@Component({
  selector: 'app-lbvs-cmdb',
  templateUrl: './lbvs-cmdb.component.html',
  styleUrl: './lbvs-cmdb.component.scss'
})
export class LbvsCmdbComponent {

  columnsToDisplay = ['id', 'aplicacion', 'nombreSVLB'];
  dataLBvsCMDB: resultado[] = [];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){

    this.apiService.getDataLBvsCMDB().subscribe(dataLBvsCMDB => {
      this.dataLBvsCMDB = dataLBvsCMDB;
    })
  }

}
