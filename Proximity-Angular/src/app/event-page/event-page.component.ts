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
    title: "Sand Volleyball",
    owner: "Pauly D", 
    time: "12:00",
    distance: "1.0 miles away",
  },
  {
    title: "Rave",
    owner: "DeadMau5", 
    time: "1:00",
    distance: "1.0 miles away",
  },
];

  ngOnInit() {
  }

}
