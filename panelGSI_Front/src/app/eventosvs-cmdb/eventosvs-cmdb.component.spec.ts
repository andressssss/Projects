import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventosvsCmdbComponent } from './eventosvs-cmdb.component';

describe('EventosvsCmdbComponent', () => {
  let component: EventosvsCmdbComponent;
  let fixture: ComponentFixture<EventosvsCmdbComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventosvsCmdbComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EventosvsCmdbComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
