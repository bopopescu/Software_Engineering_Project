import { Component, OnInit, Input } from '@angular/core';
import { Post } from '../models/post';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  constructor(private userService: UserService, private dataService: DataService) { }

  @Input() post: Post

  ngOnInit() {
  }

  displayComments() {
		this.post.displayComments = !this.post.displayComments;
  }
  
  like(){

  }

  dislike(){

  }

  comment(){

  }
}
