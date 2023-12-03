import { TestBed } from '@angular/core/testing';

import { ErorrServiceService } from './erorr-service.service';

describe('ErorrServiceService', () => {
  let service: ErorrServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ErorrServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
