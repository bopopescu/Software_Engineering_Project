//written by: John Oatey
import { Component, OnInit,Input } from '@angular/core';
import { Message } from '../models/message';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.css']
})
export class MessageComponent implements OnInit {

  constructor(private userService: UserService, private dataService: DataService) { }

  @Input() message: Message

  ngOnInit() {
  }

}
