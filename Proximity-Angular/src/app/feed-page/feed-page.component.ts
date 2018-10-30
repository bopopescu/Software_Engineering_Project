import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.css', '../app.component.css']

  


})
export class FeedPageComponent implements OnInit {

  constructor(private dataService: DataService) { }

  posts:Observable<any>;

  ngOnInit() {
    navigator.geolocation.getCurrentPosition(position => {
      this.dataService.getFeed(position.coords.latitude, position.coords.longitude)
      .subscribe(posts => {
        console.log(posts);
        this.posts = posts;
      })
    })
  }
}