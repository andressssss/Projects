import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CmdbvsLbComponent } from './cmdbvs-lb.component';

describe('CmdbvsLbComponent', () => {
  let component: CmdbvsLbComponent;
  let fixture: ComponentFixture<CmdbvsLbComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CmdbvsLbComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CmdbvsLbComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
