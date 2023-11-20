import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAllAbonementComponent } from './list-all-abonement.component';

describe('ListAllAbonementComponent', () => {
  let component: ListAllAbonementComponent;
  let fixture: ComponentFixture<ListAllAbonementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListAllAbonementComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListAllAbonementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
