import { TestBed } from '@angular/core/testing';

import { DistanceService } from './distance.service';
import { componentFactoryName } from '@angular/compiler';
import { Location } from '../models/location'

describe('DistanceService', () => {
  let service: DistanceService;
  beforeEach(() =>{ 
    service = new DistanceService();
    TestBed.configureTestingModule({})
  }); 

  it('should be created', () => {
    const service: DistanceService = TestBed.get(DistanceService);
    expect(service).toBeTruthy();
  });

  fdescribe('calculateDistance ', () => {
    it('given lat1, lat2, long1, long2, should return distance', () => {
      let location1: Location = {
        lat: 2.9,
        long: 2.000
      }
      let location2: Location = {
        lat: 4.9,
        long: 49.2
      }
      var distance = service.getDistance(location1, location2);
      distance /= 10;
      distance = Math.floor(distance);
      distance *= 10;
      expect(distance).toBe(3250);
    })
  });
});
