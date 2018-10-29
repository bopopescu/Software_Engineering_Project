import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FeedPageComponent } from './feed-page.component';
import { HttpClientModule } from '@angular/common/http';
import { DataService } from '../data.service';

describe('FeedPageComponent', () => {
  let component: FeedPageComponent;
  let fixture: ComponentFixture<FeedPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FeedPageComponent ],
      imports: [ HttpClientModule ],
      providers: [ DataService ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FeedPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
