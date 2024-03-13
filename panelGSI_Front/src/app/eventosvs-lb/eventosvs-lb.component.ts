import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-eventosvs-lb',
  templateUrl: './eventosvs-lb.component.html',
  styleUrl: './eventosvs-lb.component.scss'
})
export class EventosvsLbComponent {
  dataEvevsLB: any[] = [];
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVEventos'];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataEvevsLB().subscribe(dataEvevsLB => {
      this.dataEvevsLB = dataEvevsLB;
      console.log(this.dataEvevsLB);
    })
  }
}
