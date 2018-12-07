import { Component, OnInit, Input } from '@angular/core';
import { Post } from '../models/post';
import { UserService } from '../services/user.service';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';
import { CreateCommentDialogComponent } from '../create-comment-dialog/create-comment-dialog.component';
import { MatDialog } from '@angular/material';
import { User } from '../models/user';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  constructor(private userService: UserService, private dataService: DataService,
    private dialog: MatDialog) { }

  @Input() post: Post
  // @Input() user: User
  comments: Array<Comment>

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

  createComment(){
    const dialogRef = this.dialog.open(CreateCommentDialogComponent);
    dialogRef.afterClosed().subscribe(data => {
      this.dataService.createComment(this.post.id, data);
    })
  }
}
