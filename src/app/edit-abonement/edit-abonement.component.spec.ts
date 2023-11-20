import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAbonementComponent } from './edit-abonement.component';

describe('EditAbonementComponent', () => {
  let component: EditAbonementComponent;
  let fixture: ComponentFixture<EditAbonementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditAbonementComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditAbonementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
