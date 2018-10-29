import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../data.service';

@Component({
	selector: 'app-login-page',
	templateUrl: './login-page.component.html',
	styleUrls: ['../app.component.css']
})
export class LoginPageComponent implements OnInit {

	constructor(private fb: FormBuilder, private dataService: DataService) { }

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
		this.dataService.login(this.user);
	}
}

