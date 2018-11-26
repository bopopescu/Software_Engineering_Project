import { Component, OnInit, NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css']
})


export class AppComponent{
	constructor(){

	}
	str = '<li class="navItem">Logout</li>';
	logoutDisplay(){
		if(sessionStorage.getItem('currentUser')){
			return this.str;
	}
	}
}
