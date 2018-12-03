import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';
import { Post } from '../models/post';
import { PositionStrategy } from '@angular/cdk/overlay';

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.css', '../app.component.css']
})
export class FeedPageComponent implements OnInit {

  constructor(private dataService: DataService) { }
  
  posts: Observable<Post>;
  ngOnInit() {
    navigator.geolocation.getCurrentPosition(position => {
      this.dataService.getFeed(position.coords.latitude, position.coords.longitude)
      .subscribe(posts => {
        this.posts = posts.posts;
        console.log(this.posts);
      })
    })
  }
}