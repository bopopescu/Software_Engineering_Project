import { Injectable } from '@angular/core';
import { Location } from '../models/location'

@Injectable({
  providedIn: 'root'
})
export class DistanceService {

  constructor() { }

  getDistance(location1: Location, location2: Location){
    var R = 6371e3; // metres
    var pi = Math.PI;
    var toRadians = pi/180;
    var φ1 = +location1.lat * toRadians; 
    var φ2 = +location2.lat * toRadians;
    var Δφ = (+location2.lat- +location1.lat) * toRadians;
    var Δλ = (+location2.long - +location1.long) * toRadians;

    var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
        Math.cos(φ1) * Math.cos(φ2) *
        Math.sin(Δλ/2) * Math.sin(Δλ/2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

    var distance = R * c;
    distance /= 1000;
    distance *= 0.621371;

    return distance;
  }
}
