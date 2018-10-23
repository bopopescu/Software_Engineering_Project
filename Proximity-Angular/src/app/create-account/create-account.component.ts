import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})

export class CreateAccountComponent implements OnInit {
  isValid: Boolean;

  constructor(private fb: FormBuilder) {
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
    let passwordCheck = this.createAccount.get('password').value;

    if(password == passwordCheck){
      this.isValid = true;
    }
    else{
      this.isValid = false;
    }
  }
  ngOnInit() {
  }

}
