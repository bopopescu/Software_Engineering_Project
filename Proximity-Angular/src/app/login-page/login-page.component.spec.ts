import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginPageComponent } from './login-page.component';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { log } from 'util';
import { DataService } from '../data.service';
import { HttpClientModule } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { DebugElement } from '@angular/core';

describe('LoginPageComponent', () => {
	let component: LoginPageComponent;
	let fixture: ComponentFixture<LoginPageComponent>;
	let debugElement: DebugElement;
	let dataService: DataService;
	let dataServiceSpy;

	beforeEach(async(() => {
		TestBed.configureTestingModule({
			imports: [ReactiveFormsModule, HttpClientModule],
			declarations: [LoginPageComponent],
			providers: [FormBuilder, DataService, {provide: ActivatedRoute, useValue: '/' },
			 { provide: Router, useClass: class {router = jasmine.createSpy('router')}} ]	
		})
			.compileComponents();
	}));

	beforeEach(() => {
		fixture = TestBed.createComponent(LoginPageComponent);
		component = fixture.componentInstance;
		fixture.detectChanges();

		debugElement = fixture.debugElement;
		dataService = debugElement.injector.get(DataService);
    	dataServiceSpy = spyOn(dataService, 'login');
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
