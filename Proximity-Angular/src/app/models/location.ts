export class Location {
    info: string;
    latitude: number;
    longitude: number;

    constructor(info: string, latitude: number, longitude: number){
        this.info = info;
        this.latitude = latitude;
        this.longitude = longitude;
    }
}