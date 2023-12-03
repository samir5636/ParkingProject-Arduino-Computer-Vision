import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RefrechAbonementComponent } from './refrech-abonement.component';

describe('RefrechAbonementComponent', () => {
  let component: RefrechAbonementComponent;
  let fixture: ComponentFixture<RefrechAbonementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RefrechAbonementComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RefrechAbonementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
