import { Component, OnInit, NgModule, OnChanges } from '@angular/core';
import { AuthGuard } from './services/auth.guard';
import { Router } from '@angular/router';
import {MatDialog} from '@angular/material';
import {LogoutDialogComponent} from './logout-dialog/logout-dialog.component'
import { UserService } from './services/user.service';
import { Observable } from 'rxjs';
import { User } from './models/user';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css']
})


export class AppComponent{
	constructor(private userService: UserService, private auth: AuthGuard, private router: Router, public dialog: MatDialog){
		// this.loggedIn = true;
		// this.router.events.subscribe( () =>{
		// 	this.loggedIn = this.auth.isLoggedIn();
		// 	if(this.loggedIn){
		// 		this.id = this.userService.getId();
		// 	}
	
		// 	console.log("Woooo");
		// })
		this.user = this.userService.getUser();
	}

	loggedIn: Boolean
	id: Number
	user: User

	loginDialog(){
		if(this.loggedIn){
			this.dialog.open(LogoutDialogComponent);
		}
		else{
			this.router.navigateByUrl("/login");
		}
	}

}
