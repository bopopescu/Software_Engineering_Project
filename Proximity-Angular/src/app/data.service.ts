import { Injectable } from '@angular/core';
import { User } from './models/user';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { LoginResponse } from './models/login-response';
import { Location } from './models/location';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { 

  }
  baseUrl = 'http://104.42.175.128';


  login(user: User){
    return this.http.post<any>(this.baseUrl + '/account/v1/login', user)
      .pipe( map(usr => {
        if (usr && usr.token) {
          sessionStorage.setItem('currentUser', JSON.stringify(usr));
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

  getFriends(): Observable<Location[]>{
    return this.http.get<Location[]>(this.baseUrl + '/account/v1/friends/fetch')
  }

  getFeed(): Observable<string[]>{
    return this.http.get<string[]>(this.baseUrl + '/feed/v1/fetch');
  }

}
