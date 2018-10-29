import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../data.service';
import { Router, ActivatedRoute } from '@angular/router';
import { first } from 'rxjs/operators';


@Component({
	selector: 'app-login-page',
	templateUrl: './login-page.component.html',
	styleUrls: ['../app.component.css']
})
export class LoginPageComponent implements OnInit {

	constructor(private fb: FormBuilder, private dataService: DataService, private route: ActivatedRoute, private router: Router) { }
	returnUrl: string;

	loginForm = this.fb.group({
		username: ['', Validators.required],
		password: ['', Validators.required]
	})

	user: User;

	ngOnInit(): void {
		this.dataService.logout();
		this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
	}

	onSubmit() {
		this.user = new User();
		navigator.geolocation.getCurrentPosition(
			(position) => {
				console.log(position);
				this.user.latitude = position.coords.latitude;
				this.user.latitude = position.coords.longitude;
				this.user.username = this.loginForm.get('username').value;
				this.user.password = this.loginForm.get('password').value;
				this.dataService.login(this.user)
				.pipe(first())
				.subscribe( response => {
					console.log(response);
					this.router.navigate([this.returnUrl]);
				},
				error =>{
					console.log(error);
				})
			},
			() => {
				console.log('Unable to get location');
			}
		);
	}
}

