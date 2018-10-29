import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginPageComponent } from './login-page.component';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { log } from 'util';
import { DataService } from '../data.service';
import { HttpClientModule } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';

describe('LoginPageComponent', () => {
	let component: LoginPageComponent;
	let fixture: ComponentFixture<LoginPageComponent>;

	beforeEach(async(() => {
		TestBed.configureTestingModule({
			imports: [ReactiveFormsModule, HttpClientModule],
			declarations: [LoginPageComponent],
			providers: [FormBuilder, DataService, ActivatedRoute, Router]	
		})
			.compileComponents();
	}));

	beforeEach(() => {
		fixture = TestBed.createComponent(LoginPageComponent);
		component = fixture.componentInstance;
		fixture.detectChanges();
	});

	it('should create', () => {
		expect(component).toBeTruthy();
	});

	describe('Validation: ', () => {
		it('username should have a value', () => {
			var username = component.loginForm.get('username');
			username.setValue('Jackoman100');
			expect(username.valid).toBe(true);
		});

		it('password should have a value ', () => {
			var password = component.loginForm.get('password');
			password.setValue('password');
			expect(password.valid).toBe(true);
		})
	});
});
