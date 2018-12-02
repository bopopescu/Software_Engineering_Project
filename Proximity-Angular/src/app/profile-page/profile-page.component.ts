import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Observable } from "rxjs";
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

	oprofile: Observable<User>;
	profile: User
	notFriend: Boolean
	id: Number

	ngOnInit() {
		this.id = Number.parseInt(this.activatedRoute.snapshot.url[1].path);
		this.profileData.disable();
		if(this.id !== 5){
			this.profileData.get('createPost').disable();
		}
		this.dataService.getProfileInfo(this.id)
		  .subscribe(info => {
		    this.oprofile = info;
		  })

		setTimeout(() => {
			if (this.id == 5) {
				var thing: Comment;
				thing = {
					body: "My comment has stuff in it",
					name: "Hanna Montana"
				}
				var array: Array<Comment> = [thing];
				this.profile = {
					firstName: "Miley",
					lastName: "Cyrus",
					id: 5,
					email: "WreckingHoes@Career.gov",
					distance: 50,
					posts: [
						{
							body: "Something I just wonder what would have happened if I focused more on my career.",
							name: "Miley Cyrus",
							title: "My career is a dump now...",
							displayComments: false,
							comments: array,
							userId: 5,
							postId: 2,
							distance: 20
						},
						{
							body: "Something something daddy issues. JKFDS:JFK:LDFJSK L: Jfkljfakldsfj iaj eilj afis;j flsakjiewjo pdjfkad;slfj a;sdjfs da;fjkas; fjdakl ;fj",
							name: "Miley Cyrus",
							title: "My dad sucks",
							displayComments: false,
							userId: 5,
							postId: 1,
							distance: 50
						}
					],
					fullName: "Miley Cyrus"
				}
				console.log(this.profile);
			}
		}, 10);
	}

	createPost() {
		this.dialog.open(CreatePostDialogComponent,{
			data: {
				name: this.profile.fullName
			}
		});
	}
}