/// <reference types="@types/googlemaps" />
import { Component, OnInit } from '@angular/core';
import { ViewChild } from '@angular/core';
import { Observable } from "rxjs";
import { Location } from "../models/location"
import { DataService } from '../data.service';
import { Router } from '@angular/router';

@Component({
	selector: 'app-map-page',
	templateUrl: './map-page.component.html',
	styleUrls: ['../app.component.css', './map-page.component.css']
})


export class MapPageComponent implements OnInit {
	constructor(private router: Router, private dataService: DataService ) {
	}

	@ViewChild('gmap') gmapElement: any;
	map: google.maps.Map;

	latitude: any;
	longitude: any;
	friendMarkers: google.maps.Marker[] = [];
	groupMarkers: google.maps.Marker[];

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
		this.dataService.getFriends()
			.subscribe(
				locations => {
					var loc = locations.friends;
					for (var i = 0; i < loc.length; i++) {
						var position = new google.maps.LatLng(loc[i].latitude, loc[i].longitude);
						var contentString =
							'<p><b>Name</b>: ' + loc[i].name + '</br>' +
							'<b>Distance</b>: ' + loc[i].distance + '</br>' +
							'</p>';
						var infoWindow = new google.maps.InfoWindow({
							content: contentString
						})

						var marker = new google.maps.Marker({
							position: position,
							map: this.map
						})

						marker.addListener('click', () => {
							this.router.navigateByUrl('/profile/' + loc.id);
						});

						marker.addListener('mouseover', () => {
							infoWindow.open(this.map, marker);
						});

						marker.addListener('mouseout', () => {
							infoWindow.close();
						});
						setTimeout(() => {
							this.friendMarkers.push(marker);
						}, 100);
					}
				}
			)
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
		var loc = {
			name: "bob",
			distance: 32.7,
			latitude: 38.951706,
			longitude: -92.334068,
			id: 1

		}
		var position = new google.maps.LatLng(loc.latitude, loc.longitude);
						var contentString =
							'<p><b>Name</b>: ' + loc.name + '</br>' +
							'<b>Distance</b>: ' + loc.distance + '</br>' +
							'</p>';
						var infoWindow = new google.maps.InfoWindow({
							content: contentString
						})

						var marker = new google.maps.Marker({
							position: position,
							map: this.map
						})

						marker.addListener('click',() => {
							this.router.navigateByUrl("/profile/" + loc.id);
						});

						marker.addListener('mouseover', () => {
							infoWindow.open(this.map, marker);
						});

						marker.addListener('mouseout',() => {
							infoWindow.close();
						});
	}
}
