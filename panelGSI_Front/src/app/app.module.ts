import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { HttpClientModule } from '@angular/common/http';
import { MatCardModule} from '@angular/material/card';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { MatTableModule } from '@angular/material/table';
import { MatDividerModule } from '@angular/material/divider';
import { LBvsEventosComponent } from './lbvs-eventos/lbvs-eventos.component';
import { CMDBvsEventosComponent } from './cmdbvs-eventos/cmdbvs-eventos.component';
import { MatBadgeModule } from '@angular/material/badge';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatTooltipModule } from '@angular/material/tooltip';
import { CmdbvsLbComponent } from './cmdbvs-lb/cmdbvs-lb.component';
import { EventosvsLbComponent } from './eventosvs-lb/eventosvs-lb.component';
import { LbvsCmdbComponent } from './lbvs-cmdb/lbvs-cmdb.component';
import { EventosvsCmdbComponent } from './eventosvs-cmdb/eventosvs-cmdb.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatPaginatorModule} from '@angular/material/paginator';
import {ClipboardModule} from '@angular/cdk/clipboard';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LBvsEventosComponent,
    CMDBvsEventosComponent,
    CmdbvsLbComponent,
    EventosvsLbComponent,
    LbvsCmdbComponent,
    EventosvsCmdbComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatSlideToggleModule,
    HttpClientModule,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule,
    NgbModule,
    MatTableModule,
    MatDividerModule,
    MatBadgeModule,
    MatGridListModule,
    MatTooltipModule,
    MatFormFieldModule,
    MatInputModule,
    MatPaginatorModule,
    ClipboardModule
  ],
  providers: [
    provideAnimationsAsync(),
    LBvsEventosComponent,
    CMDBvsEventosComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
