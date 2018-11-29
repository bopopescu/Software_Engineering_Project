import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { CreateAccountComponent } from './create-account.component';
import { HttpClientModule } from '@angular/common/http';
import { DataService } from '../services/data.service';
import { DebugElement } from '@angular/core';

describe('CreateAccountComponent', () => {
  let component: CreateAccountComponent;
  let fixture: ComponentFixture<CreateAccountComponent>;
  let debugElement: DebugElement;
  let dataService: DataService;
  let dataServiceSpy;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateAccountComponent ],
      imports: [ReactiveFormsModule, HttpClientModule],
      providers: [ DataService ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateAccountComponent);
    debugElement = fixture.debugElement;
    component = fixture.componentInstance;
    fixture.detectChanges();

    dataService = debugElement.injector.get(DataService);
    dataServiceSpy = spyOn(dataService, 'createAccount');
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  describe('onSubmit ', () => {

    it('given password and passwordCheck do not match, isValid should be false', () => {
      var password = component.createAccount.get('password');
      var passwordCheck = component.createAccount.get('passwordCheck');
      password.setValue('potatoe');
      passwordCheck.setValue('potatooooooo');
      component.onSubmit();
      expect(component.isValid).toBe(false);
    });
    
    it('given password and passwordCheck match, isValid should be true, DataService should be called', () => {
      component.isValid = false;

      var password = component.createAccount.get('password');
      var passwordCheck = component.createAccount.get('passwordCheck');
      password.setValue('potatoe');
      passwordCheck.setValue('potatoe');
      component.onSubmit();
      expect(dataServiceSpy).toHaveBeenCalled();
      expect(component.isValid).toBe(true);
    });
  });
});
