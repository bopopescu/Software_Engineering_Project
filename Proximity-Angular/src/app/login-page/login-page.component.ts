import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../services/data.service';
import { Router, ActivatedRoute } from '@angular/router';
import { first } from 'rxjs/operators';
import { UserService } from '../services/user.service';
import { User } from '../models/user';


@Component({
	selector: 'app-login-page',
	templateUrl: './login-page.component.html',
	styleUrls: ['../app.component.css']
})
export class LoginPageComponent implements OnInit {

	constructor(private fb: FormBuilder, private userService: UserService, private dataService: DataService, private route: ActivatedRoute, private router: Router) { }
	returnUrl: string;

	loginForm = this.fb.group({
		username: ['', Validators.required],
		password: ['', Validators.required]
	})

	user: any;

	ngOnInit(): void {
		// this.dataService.logout();
	}

	onSubmit() {
		this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
		
		navigator.geolocation.getCurrentPosition(
			(position) => {
				console.log(position);
				var user = {
					latitude: position.coords.latitude,
					longitude: position.coords.longitude,
					username: this.loginForm.get('username').value,
					password: this.loginForm.get('password').value
				}
				this.dataService.login(this.user)
				.pipe(first())
				.subscribe( response => {
					console.log("Successful Login");
					var user: User = {
						firstName: response.firstName,
						lastName: response.lastName,
						email: response.email,
						id: response.id,
						fullName: response.fullName
					}
					this.userService.setUser(user);
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

