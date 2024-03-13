import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CMDBvsEventosComponent } from './cmdbvs-eventos.component';

describe('CMDBvsEventosComponent', () => {
  let component: CMDBvsEventosComponent;
  let fixture: ComponentFixture<CMDBvsEventosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CMDBvsEventosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CMDBvsEventosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
