/// <reference types="@types/googlemaps" />
import { Component, OnInit } from '@angular/core';
import { ViewChild } from '@angular/core';
import { Observable } from "rxjs";
import { Location } from "../models/location"
import { DataService } from '../data.service';

@Component({
	selector: 'app-map-page',
	templateUrl: './map-page.component.html',
	styleUrls: ['./map-page.component.css', '../app.component.css']
})


export class MapPageComponent implements OnInit {
	constructor(private dataService: DataService) { }
	$locations: Observable<Location[]>;

	@ViewChild('gmap') gmapElement: any;
	map: google.maps.Map;

	latitude: any;
	longitude: any;
	friendMarkers: google.maps.Marker[];
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

		var friends = this.dataService.getFriends();
		friends.subscribe(
			locations => {
				for (var i = 0; i < this.friendMarkers.length; i++) {
					this.friendMarkers[i].setMap(null);
					this.friendMarkers.length = 0;
				}
				for (var i = 0; i < locations.length; i++) {
					var position = new google.maps.LatLng(locations[i].latitude, locations[i].longitude);
					var marker = new google.maps.Marker({
						position: position,
						map: this.map
					})
					this.friendMarkers.push(marker);
				}
			})

		//  this.httpClient.get<Location[]>("url").subscribe(
		//   locations => {
		//     for(var i = 0;i < this.groupMarkers.length; i++){
		//       this.groupMarkers[i].setMap(null);
		//       this.groupMarkers.length = 0;
		//     }
		//     for(var i = 0; i < locations.length; i++){
		//       var position = new google.maps.LatLng(locations[i].latitude, locations[i].longitude);
		//       var marker = new google.maps.Marker({
		//         position: position,
		//         map: this.map
		//       })
		//       this.groupMarkers.push(marker);
		//     }
		// })
	}

	initMap() {
		var mapProp;
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(
				position => {
					this.latitude = position.coords.latitude;
					this.longitude = position.coords.longitude;
					mapProp = {
						center: new google.maps.LatLng(this.latitude, this.longitude),
						zoom: 15,
						mapTypeId: google.maps.MapTypeId.ROADMAP
					}
					this.map = new google.maps.Map(this.gmapElement.nativeElement, mapProp);
				}
			)
		}
		else {
			mapProp = {
				center: new google.maps.LatLng(0, 0),
				zoom: 15,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};
		this.map = new google.maps.Map(this.gmapElement.nativeElement, mapProp);
		}
	}
}
