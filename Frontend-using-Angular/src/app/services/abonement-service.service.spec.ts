import { TestBed } from '@angular/core/testing';

import { AbonementServiceService } from './abonement-service.service';

describe('AbonementServiceService', () => {
  let service: AbonementServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AbonementServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
