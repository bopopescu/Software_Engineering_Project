import { Component, OnInit } from '@angular/core';
import { Event } from '../models/event';
import { Observable } from 'rxjs';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-event-page',
  templateUrl: './event-page.component.html',
  styleUrls: ['./event-page.component.css']
})
export class EventPageComponent implements OnInit {

  constructor(private dataService: DataService) { }

  events = [{
    title: "Donald",
    owner: "Healthy young child goes to doctor, gets pumped with massive shot of many vaccines, doesn’t feel good and changes – AUTISM. Many such cases!", 
    time: "TRUTH, YOU WONT BELIEVE",
    distance: "1.0 miles away",
  },
  {
    title: "Donald",
    owner: "Every time I speak of the haters and losers I do so with great love and affection. They cannot help the fact that they were born fucked up!", 
    time: "CANT BELIEVE THIS COUNTRY",
    distance: "1.0 miles away",
  },
];

  ngOnInit() {
  }

}
