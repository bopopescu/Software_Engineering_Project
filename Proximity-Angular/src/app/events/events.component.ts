import { Component, OnInit,Input } from '@angular/core';
import { Event } from '../models/event';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  constructor(private userService: UserService, private dataService: DataService) { }

  @Input() event: Event

  ngOnInit() {
  }

}
