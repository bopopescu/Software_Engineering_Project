import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
	selector: 'app-create-account',
	templateUrl: './create-account.component.html',
	styleUrls: ['./create-account.component.css']
})

export class CreateAccountComponent implements OnInit {
	isValid: Boolean;

	constructor(private fb: FormBuilder, private httpClient: HttpClient) {
		this.isValid = true;
	}
	createAccount = this.fb.group({
		username: [''],
		password: [''],
		passwordCheck: [''],
		email: ['']
	})

	onSubmit() {
		let password = this.createAccount.get('password').value;
		let passwordCheck = this.createAccount.get('passwordCheck').value;

		if (password == passwordCheck) {
			this.isValid = true;
		}
		else {
			this.isValid = false;
		}
		var account = {
			password: password,
			username: this.createAccount.get('username').value
		}

		this.httpClient.post('104.42.175.128/login', account)
			.subscribe(
				response => 
					console.log(response),
				error => 
					console.log(error)
			)
	}
	ngOnInit() {
	}

}
