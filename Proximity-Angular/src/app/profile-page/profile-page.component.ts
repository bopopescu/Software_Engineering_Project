//written by: John Oatey
import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Observable, config } from "rxjs";
import { User } from '../models/user';
import { UserService } from '../services/user.service';
import { Post } from '../models/post';
import { Comment } from '../models/comment';
import {MatDialog} from '@angular/material';
import { CreatePostDialogComponent } from '../create-post-dialog/create-post-dialog.component';


@Component({
	selector: 'app-profile-page',
	templateUrl: './profile-page.component.html',
	styleUrls: ['./profile-page.component.css', '../app.component.css']
})
export class ProfilePageComponent implements OnInit {

	constructor(private dataService: DataService, private activatedRoute: ActivatedRoute
		, private fb: FormBuilder, private userService: UserService, private dialog: MatDialog) { }

	profileData = this.fb.group({
		firstName: [''],
		lastName: [''],
		email: [''],
		createPost: ['']
	})

	profile: User
	notFriend: Boolean
	id: Number

	ngOnInit() {
		this.id = Number.parseInt(this.activatedRoute.snapshot.url[1].path);
		this.profileData.disable();
		if(this.id !== this.userService.id){
			this.profileData.get('createPost').disable();
		}
		this.dataService.getProfileInfo(this.id)
		  .subscribe(response => {
			this.profile = response;
			this.profileData.get('firstName').setValue(response.first_name);
			this.profileData.get('lastName').setValue(response.last_name);
		  })
		this.dataService.getPost(this.id)
		  .subscribe(response => {
			  console.log(response);
			  this.profile.posts = response.posts;
		  })
		
	}

	createPost() {
		const dialogRef = this.dialog.open(CreatePostDialogComponent,{
			height: '400px',
			width: '600px',
			data: {
				name: this.profile.full_name
			}
		},
		);
		dialogRef.afterClosed().subscribe(body => {
			if(this.profile.posts === null){
				this.profile.posts = new Array<Post>();
			}
			var post: Post = {
				body: body.get('body').value,
				distance: 0.00,
				id: 0,
				time: Date.now(),
				title: body.get('title').value,
				username: "irrelevant",
				user: this.profile
			}
			this.dataService.createPost(post).subscribe( data => {
				console.log(data);
			}) 
			// this.profile.posts.push(post);
		})
	}
}