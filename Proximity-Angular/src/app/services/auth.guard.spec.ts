import { TestBed, async, inject } from '@angular/core/testing';

import { AuthGuard } from './auth.guard';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

describe('AuthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AuthGuard, HttpClient, {provide: Router, useClass: class { navigate = jasmine.createSpy("navigate");}}]
    });
  });

  it('should ...', inject([AuthGuard], (guard: AuthGuard) => {
    expect(guard).toBeTruthy();
  }));
});
