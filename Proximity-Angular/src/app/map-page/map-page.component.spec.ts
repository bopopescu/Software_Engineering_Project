/// <reference types="@types/googlemaps" />
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MapPageComponent } from './map-page.component';
import { HttpClientModule } from '@angular/common/http';
import { DataService } from '../data.service';
import { cold, getTestScheduler } from 'jasmine-marbles';


describe('MapPageComponent', () => {
	let component: MapPageComponent;
	let fixture: ComponentFixture<MapPageComponent>;

	beforeEach(async(() => {
		TestBed.configureTestingModule({
			declarations: [ MapPageComponent ],
			imports: [HttpClientModule],
			providers: [ { provide: DataService } ]
		})
			.compileComponents();
	}));

	// const dataServiceStub = {
	// 	get() {
	// 		const locations = cold('--x', 
	// 			{
	// 				latitude: 5,
	// 				longitude: -2,
	// 				info: "Skittles are better than m&ms"
	// 			}
	// 		);
	// 	}
	// }

	beforeEach(() => {
		fixture = TestBed.createComponent(MapPageComponent);
		component = fixture.componentInstance;
		fixture.detectChanges();
	});

	it('should create', () => {
		expect(component).toBeTruthy();
	});

	// describe('Map ', () => {
	// 	it('given friends should populate friendMarkers', () => {
	// 	})
	// })
});
