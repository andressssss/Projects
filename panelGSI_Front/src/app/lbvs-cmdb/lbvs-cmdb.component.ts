import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-lbvs-cmdb',
  templateUrl: './lbvs-cmdb.component.html',
  styleUrl: './lbvs-cmdb.component.scss'
})
export class LbvsCmdbComponent {

  dataLBvsCMDB: any[] = [];
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVLB'];

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
