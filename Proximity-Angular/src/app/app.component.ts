import { Component, OnInit, NgModule } from '@angular/core';
import { MatSidenav, MatSidenavContent, MatSidenavContainer } from 'angular-material';
import { AuthGuard } from './auth.guard';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css']
})


export class AppComponent{
	constructor(private auth: AuthGuard){}
	shouldRun = true;
	
}
