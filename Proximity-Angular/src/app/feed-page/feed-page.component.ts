import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.css', '../app.component.css']
})
export class FeedPageComponent implements OnInit {

  constructor(private dataService: DataService) { }

  posts = [{
    user: "Donald",
    body: "Healthy young child goes to doctor, gets pumped with massive shot of many vaccines, doesn’t feel good and changes – AUTISM. Many such cases!", 
    title: "TRUTH, YOU WONT BELIEVE",
    distance: "1.0 miles away",
  },
  {
    user: "Donald",
    body: "Every time I speak of the haters and losers I do so with great love and affection. They cannot help the fact that they were born fucked up!", 
    title: "CANT BELIEVE THIS COUNTRY",
    distance: "1.0 miles away",
  },
];

  ngOnInit() {
    // navigator.geolocation.getCurrentPosition(position => {
    //   this.dataService.getFeed(position.coords.latitude, position.coords.longitude)
    //   .subscribe(posts => {
    //     this.posts = posts.posts;
    //   })
    // })
  }
}