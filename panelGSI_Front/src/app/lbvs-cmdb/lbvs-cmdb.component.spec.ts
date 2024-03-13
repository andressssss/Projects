import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LbvsCmdbComponent } from './lbvs-cmdb.component';

describe('LbvsCmdbComponent', () => {
  let component: LbvsCmdbComponent;
  let fixture: ComponentFixture<LbvsCmdbComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LbvsCmdbComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LbvsCmdbComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
