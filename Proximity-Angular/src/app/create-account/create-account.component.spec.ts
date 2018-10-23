import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { CreateAccountComponent } from './create-account.component';

describe('CreateAccountComponent', () => {
  let component: CreateAccountComponent;
  let fixture: ComponentFixture<CreateAccountComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateAccountComponent ],
      imports: [ReactiveFormsModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateAccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
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
    
    it('given password and passwordCheck match, isValid should be true', () => {
      component.isValid = false;

      var password = component.createAccount.get('password');
      var passwordCheck = component.createAccount.get('passwordCheck');
      password.setValue('potatoe');
      passwordCheck.setValue('potatoe');
      component.onSubmit();
      expect(component.isValid).toBe(true);
    });
  });
});
