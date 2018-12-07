/// <reference types="@types/googlemaps" />
import { Component, OnInit } from '@angular/core';
import { ViewChild } from '@angular/core';
import { Observable } from "rxjs";
import { DataService } from '../services/data.service';
import { Router } from '@angular/router';
import { FormBuilder} from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import {Event} from "../models/event"
import { UserService } from '../services/user.service';


@Component({
	selector: 'app-map-page',
	templateUrl: './map-page.component.html',
	styleUrls: ['../app.component.css', './map-page.component.css']
})


export class MapPageComponent implements OnInit {
	constructor(private fb: FormBuilder,private router: Router, private dataService: DataService, private userService: UserService) {
		this.markers = new Array<google.maps.Marker>();
	}

	searchBar = this.fb.group({
		search: ['']
	})

	@ViewChild('gmap') gmapElement: any;
	map: google.maps.Map;

	latitude: any;
	longitude: any;
	friendMarkers: google.maps.Marker[] = [];
	groupMarkers: google.maps.Marker[];
	markers: google.maps.Marker[];
	results: Observable<google.maps.Marker[]>;

	iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';

	markerTypes = [
		{
			text: "Parking", value: "parking_lot_maps.png"
		}
	];

	selectedMarkerType: string = "parking_lot_maps.png";

	isHidden = false;

	ngOnInit() {
		this.initMap();
		this.results = this.searchBar.get('search').valueChanges
			.pipe(
				startWith(''),
				map(value => {
					return this.filterSearch(value)
				}));
		this.dataService.getFriends()
			.subscribe(
				locations => {
					var loc = locations.friends;
					for (var i = 0; i < loc.length; i++) {
						var position = new google.maps.LatLng(loc[i].latitude, loc[i].longitude);
						var contentString =
							'<p><b>Name</b>: ' + loc[i].full_name + '</br>' +
							'<b>Distance</b>: ' + loc[i].distance + '</br>' +
							'</p>';
						var infoWindow = new google.maps.InfoWindow({
							content: contentString
						})

						var marker = new google.maps.Marker({
							position: position,
							map: this.map,
							title: loc[i].id.toString() + "_" + loc[i].full_name
						})

						marker.addListener('click', () => {
							var id = marker.getTitle().split("_")[0];
							this.router.navigateByUrl('/profile/' + id);
						});

						marker.addListener('mouseover', () => {
							infoWindow.open(this.map, marker);
						});

						marker.addListener('mouseout', () => {
							infoWindow.close();
						});
							this.friendMarkers.push(marker);
							this.markers.push(marker);
					}
				}
			)
			
			this.dataService.getEvents(this.latitude,this.longitude)
			.subscribe(
				events => {
					this.groupMarkers = new Array<google.maps.Marker>();
					var loc = events;
					for (var i = 0; i < loc.length; i++) {
						var position = new google.maps.LatLng(loc[i].latitude, loc[i].longitude);
						var contentString =
							'<p><b>Name</b>: ' + loc[i].title + '</br>' +
							'<b>Distance</b>: ' + loc[i].distance + '</br>' +
							'</p>';
						var infoWindow = new google.maps.InfoWindow({
							content: contentString
						})

						var marker = new google.maps.Marker({
							position: position,
							map: this.map,
							title: loc[i].id.toString() + "_" + loc[i].title
						})

						marker.addListener('mouseover', () => {
							infoWindow.open(this.map, marker);
						});

						marker.addListener('mouseout', () => {
							infoWindow.close();
						});
						this.groupMarkers.push(marker);
						this.markers.push(marker);
					}
				}
			)
	}

	search() {
		var search = this.markers.find((element) => {
			return element.getTitle().split("_")[1].toLowerCase() == this.searchBar.get('search').value.toLowerCase();
		});

		if(search){
			this.map.panTo(search.getPosition());
		}
	}

	private filterSearch(value: string): google.maps.Marker[]{
		const filterValue = value.toLowerCase();

		return this.friendMarkers.filter(marker => {
			marker.getTitle().split("_")[1].toLowerCase().includes(filterValue)
		});
	}

	private initMap() {
		var mapProp = {
			center: new google.maps.LatLng(38.951706, -92.334068),
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		this.map = new google.maps.Map(this.gmapElement.nativeElement, mapProp);

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(
				position => {
					this.latitude = position.coords.latitude;
					this.longitude = position.coords.longitude;
					this.map.setCenter(new google.maps.LatLng(this.latitude, this.longitude));
				}
			)
		}

		// this.testData();
	}

	// private testData(){
	// 	var loc = {
	// 		name: "bob",
	// 		distance: 32.7,
	// 		latitude: 38.951706,
	// 		longitude: -92.334068,
	// 		id: 1

	// 	}
	// 	var position = new google.maps.LatLng(loc.latitude, loc.longitude);
	// 	var contentString =
	// 		'<p><b>Name</b>: ' + loc.name + '</br>' +
	// 		'<b>Distance</b>: ' + loc.distance + '</br>' +
	// 		'</p>';
	// 	var infoWindow = new google.maps.InfoWindow({
	// 		content: contentString
	// 	})

	// 	var marker = new google.maps.Marker({
	// 		position: position,
	// 		map: this.map,
	// 		title: loc.name,
	// 	})

	// 	marker.addListener('click', () => {
	// 		this.router.navigateByUrl("/profile/" + loc.id);
	// 	});

	// 	marker.addListener('mouseover', () => {
	// 		infoWindow.open(this.map, marker);
	// 	});

	// 	marker.addListener('mouseout', () => {
	// 		infoWindow.close();
	// 	});
	// 	this.friendMarkers.push(marker);
	// }
}
