/* References
  https://angular.io/guide/testing
  https://medium.com/paramsingh-66174/automate-e2e-testing-of-angular-4-apps-with-protractorjs-jasmine-fcf1dd9524d5
  https://docs.angularjs.org/guide/e2e-testing
  https://github.com/wallabyjs/public/issues/1768
*/
import { AppPage } from './app.po';
import { CreateAccountComponent } from '../../src/app/create-account/create-account.component';
import { FeedPageComponent } from '../../src/app/feed-page/feed-page.component';
import { LoginPageComponent } from '../../src/app/login-page/login-page.component';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DataService } from '../../src/app/data.service';
import { DebugElement } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';


// Create account page test
describe('CreateAccountComponent', () => {
  let account: CreateAccountComponent;

  it('should create', () => {
    expect(account).toBeTruthy();
  });
  describe('onSubmit ', () => {

    it('given password and passwordCheck do not match, isValid should be false', () => {
      var password = account.createAccount.get('password');
      var passwordCheck = account.createAccount.get('passwordCheck');
      password.setValue('pass');
      passwordCheck.setValue('passssssssss');
      account.onSubmit();
      expect(account.isValid).toBe(false);
    });
    
    it('given password and passwordCheck match, isValid should be true, DataService should be called', () => {
      account.isValid = false;

      var password = account.createAccount.get('password');
      var passwordCheck = account.createAccount.get('passwordCheck');
      password.setValue('pass');
      passwordCheck.setValue('pass');
      account.onSubmit();
      expect(account.isValid).toBe(true);
    });
  });
});



//login test
describe('LoginPageComponent', () => {
	let login: LoginPageComponent;

	it('should create', () => {
		expect(login).toBeTruthy();
	});

	describe('Validation: ', () => {
		it('username should have a value', () => {
			var username = login.loginForm.get('username');
			username.setValue('test');
			expect(username.valid).toBe(true);
		});

		it('password should have a value ', () => {
			var password = login.loginForm.get('password');
			password.setValue('pass');
			expect(password.valid).toBe(true);
		})
	});
});


//map test not working right now, will fix it by demo 2

//feed page test
describe('FeedPageComponent', () => {
  let feed: FeedPageComponent;

  it('should create', () => {
    expect(feed).toBeTruthy();
  });
});

