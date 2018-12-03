import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Post } from '../models/post';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { 

  }
  baseUrl = 'http://104.42.175.128';


  login(user: any){
    return this.http.post<any>(this.baseUrl + '/account/v1/login', user)
      .pipe( map(usr => {
        console.log("user: " + usr);
        if (usr && usr.token) {
          sessionStorage.setItem('currentUser', JSON.stringify(usr));
          console.log("session: " + sessionStorage.getItem('currentUser'));
        }
        return usr;
      }));
  }

  logout(){
    sessionStorage.removeItem('currentUser');
  }

  createAccount(username: string, password: string){
    var account = {
      username: username,
      password: password
    }
    this.http.post(this.baseUrl + '/account/v1/create', account)
			.subscribe(
				response => 
					console.log(response),
				error => 
					console.log(error)
			)
  }

  getFriends(): Observable<any>{
    return this.http.get<any>(this.baseUrl + '/account/v1/friends/fetch');
  }

  getProfileInfo(id: Number): Observable<any>{
    return this.http.get<any>(this.baseUrl + '/account/v1/profile/' + id);
  }

  getFeed(lat: number, long: number): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/feed/v1/fetch', {latitude: lat, longitude:long});
  }

  getComments(id: Number): Observable<any>{
    return this.http.post<any>(this.baseUrl + "/feed/v1/comments/fetch", { post_id: id });
  }

}
