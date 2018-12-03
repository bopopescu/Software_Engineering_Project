import { Component, OnInit, Input } from '@angular/core';
import { Post } from '../models/post';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  constructor(private userService: UserService, private dataService: DataService) { }

  @Input() post: Post
  comments: Observable<Comment>

  ngOnInit() { }

  displayComments() {
    this.post.displayComments = !this.post.displayComments;
    this.dataService.getComments(this.post.id).subscribe(response => {
      this.comments = response.comments;
    })
  }
  
  like(){

  }

  dislike(){

  }

  comment(){

  }
}
