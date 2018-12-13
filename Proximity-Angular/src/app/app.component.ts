//written by: John Oatey
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
		// this.loggedIn = this.auth.isLoggedIn();
		// this.router.events.subscribe( () =>{
		// 	this.loggedIn = this.auth.isLoggedIn();
		// 	if(this.loggedIn){
		// 		this.id = this.userService.getId();
		// 	}
		// })
		// this.user = this.userService.getUser();
	}

	// loggedIn: Boolean
	id: Number
	user: User

	get loggedIn(){
		return this.auth.isLoggedIn();
	}

	loginDialog(){
		if(this.loggedIn){
			const dialogRef = this.dialog.open(LogoutDialogComponent);
			// dialogRef.afterClosed().subscribe(loggedIn => {
			// 	this.loggedIn = loggedIn;
			// })
		}
		else{
			this.router.navigateByUrl("/login");
		}
	}

}
