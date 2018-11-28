import { Component, OnInit, NgModule } from '@angular/core';
import { AuthGuard } from './auth.guard';
import { Router } from '@angular/router';
import {MatDialog} from '@angular/material';
import {LogoutDialogComponent} from './logout-dialog/logout-dialog.component'

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css']
})


export class AppComponent{
	constructor(private auth: AuthGuard, private router: Router, public dialog: MatDialog){}
	
	get loggedIn(): Boolean {
		return this.auth.isLoggedIn();
	}

	loginDialog(){
		if(this.auth.isLoggedIn()){
			this.dialog.open(LogoutDialogComponent, {
			});
		}
		else{
			this.router.navigateByUrl("/login");
		}
	}
}
