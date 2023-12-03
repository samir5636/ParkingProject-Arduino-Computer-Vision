import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewAbonementComponent } from './new-abonement.component';

describe('NewAbonementComponent', () => {
  let component: NewAbonementComponent;
  let fixture: ComponentFixture<NewAbonementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewAbonementComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NewAbonementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
