import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  isValid: Boolean;

	constructor(private fb: FormBuilder, private dataService: DataService) {
		this.isValid = true;
	}
	resetPassword = this.fb.group({
		username: [''],
		password: [''],
		passwordCheck: [''],
		oldPassword: ['']
	})

	onSubmit() {
		let password = this.resetPassword.get('password').value;
		let passwordCheck = this.resetPassword.get('passwordCheck').value;

		if (password == passwordCheck) {
			this.isValid = true;
			var username = this.resetPassword.get('username').value;
      this.dataService.resetPassword(username, password);
		}
		else {
			this.isValid = false;
		}
	}
	ngOnInit() {

	}

}

