import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.css', '../app.component.css']
})
export class FeedPageComponent implements OnInit {

  messages: Observable<string[]>;
  
  constructor(private dataService: DataService) { }
  
  ngOnInit() {
    this.messages = this.dataService.getFeed();
    this.messages.subscribe();
  }

}
