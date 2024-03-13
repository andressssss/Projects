import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-eventosvs-cmdb',
  templateUrl: './eventosvs-cmdb.component.html',
  styleUrl: './eventosvs-cmdb.component.scss'
})
export class EventosvsCmdbComponent {
  dataEvevsCMDB: any[] = [];
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVEventos'];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataEvevsCMDB().subscribe(dataEvevsCMDB => {
      this.dataEvevsCMDB = dataEvevsCMDB;
    })
  }
}
