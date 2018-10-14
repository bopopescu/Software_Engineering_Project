import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})

export class CreateAccountComponent implements OnInit {

  constructor(private fb: FormBuilder) { }

  createAccount = this.fb.group({
    username: [''],
    password: [''],
    email: [''],
    
  })

  onSubmit() {
    
  }
  ngOnInit() {
  }

}
