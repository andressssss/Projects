import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-cmdbvs-lb',
  templateUrl: './cmdbvs-lb.component.html',
  styleUrl: './cmdbvs-lb.component.scss'
})
export class CmdbvsLbComponent {

  dataCMDBvsLB: any[] = [];
  columnsToDisplay = ['id', 'aplicacion', 'nombreSVCMDB'];

  constructor(private apiService: ApiService){
  }

  ngOnInit(): void {
    this.llenarData();
  }
  llenarData(){
    this.apiService.getDataCMDBvsLB().subscribe(dataCMDBvsEve => {
      this.dataCMDBvsLB = dataCMDBvsEve;
      console.log(this.dataCMDBvsLB);
    })
  }
}
