import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-messaging-page',
  templateUrl: './messaging-page.component.html',
  styleUrls: ['./messaging-page.component.css', '../app.component.css']
})
export class MessagingPageComponent implements OnInit {

  constructor(private dataService: DataService) { }

  messages = [{
    Sender: "Donald",
    Receiver: "Steven", 
    Body: "Hey buddy hows it going",
  },
  {
    Sender: "Stacey",
    Receiver: "Steven", 
    Body: "Hi :)",
  },
];


  ngOnInit() {
  }

}