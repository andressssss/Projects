import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-lbvs-eventos',
  templateUrl: './lbvs-eventos.component.html',
  styleUrl: './lbvs-eventos.component.scss'
})
export class LBvsEventosComponent {

  dataLBvsEve: any[] = [];
  totalallazosLBvsEve: number = 0;
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVLB'];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getData().subscribe(dataLBvsEve => {
      this.dataLBvsEve = dataLBvsEve;
      console.log(this.dataLBvsEve);
      this.totalallazosLBvsEve = this.dataLBvsEve.length;
      console.log(this.totalallazosLBvsEve);
    })
  }
}

