import { Injectable } from '@angular/core';
import { User } from './models/user';
import { HttpClient } from '@angular/common/http';
import { LoginResponse } from './models/login-response';
import { Location } from './models/location';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }
  baseUrl = 'http://104.42.175.128';

  login(user: User){
    var response: LoginResponse;
    this.http.post<LoginResponse>(this.baseUrl + '/login', user)
      .subscribe(res =>{
        console.log(res.message);
        response = res;
      },
			error => {
        console.log(error)
        response = error;
      });
  }

  createAccount(username: string, password: string){
    var account = {
      username: username,
      password: password
    }

    this.http.post(this.baseUrl + '/create', account)
			.subscribe(
				response => 
					console.log(response),
				error => 
					console.log(error)
			)
  }

  getFriends(): Observable<Location[]>{
    return this.http.get<Location[]>(this.baseUrl + '/friends/fetch')
  }

  getFeed(): Observable<string[]>{
    return this.http.get<string[]>(this.baseUrl + '/fetch');
  }

}
