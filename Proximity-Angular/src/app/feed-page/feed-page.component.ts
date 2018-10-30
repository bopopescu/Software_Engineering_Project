import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.css', '../app.component.css']

  


})
export class FeedPageComponent implements OnInit {

  constructor(private httpClient:HttpClient) { }

  posts:any;

  ngOnInit() {

    //pulling dummy datat from JSON created to reflect format_posts() in database_format.py
    //with the additon of profile photos, which we forgot to include in database
    this.httpClient.get<Location[]>(0).subscribe(posts => {

            console.log(JSON.parse(JSON.stringify(posts)));
            this.posts=JSON.parse(JSON.stringify(posts));
    }
    )
  }
    
}