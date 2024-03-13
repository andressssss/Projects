import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventosvsLbComponent } from './eventosvs-lb.component';

describe('EventosvsLbComponent', () => {
  let component: EventosvsLbComponent;
  let fixture: ComponentFixture<EventosvsLbComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventosvsLbComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EventosvsLbComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
