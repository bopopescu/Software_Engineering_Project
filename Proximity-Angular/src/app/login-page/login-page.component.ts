import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
	selector: 'app-login-page',
	templateUrl: './login-page.component.html',
	styleUrls: ['../app.component.css']
})
export class LoginPageComponent implements OnInit {

	constructor(private fb: FormBuilder, private httpClient: HttpClient) { }

	loginForm = this.fb.group({
		username: ['', Validators.required],
		password: ['', Validators.required]
	})

	user: User;

	ngOnInit(): void {
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
			},
			() => {
				console.log('Unable to get location');
			}
		);
		this.httpClient.post<User>('104.42.175.128/login', this.user)
			.subscribe(response => {
				console.log(response);
			},
			error => {
				console.log(error);
			});
	}
}

