import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Post } from '../models/post';
import { Comment } from '../models/comment';
import { CommentStmt } from '@angular/compiler';
//import { userInfo } from 'os';
import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient, private userService: UserService) { 

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

  resetPassword(username: string, old_password: string, new_password: string){
    var account = {
      username: username,
      old_password: old_password,
      new_password: new_password
    }
    this.http.post(this.baseUrl + '/account/v1/reset', account)
			.subscribe(
				response => 
					console.log(response),
				error => 
					console.log(error)
			)
  }

  getFriends(): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/account/v1/friends/fetch', {});
  }

  getProfileInfo(id: Number): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/account/v1/profile/' + id, {});
  }

  getEvents(lat: number, long: number): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/event/v1/fetch', {latitude: lat, longitude:long });
  }

  getFeed(lat: number, long: number): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/feed/v1/fetch', { latitude: lat, longitude:long });
  }

  getPost(id: Number): Observable<any> {
    return this.http.post<any>(this.baseUrl + '/feed/v1/fetch', {user_id: id})
  }

  getComments(id: Number): Observable<any>{
    return this.http.post<any>(this.baseUrl + "/feed/v1/comments/fetch", { post_id: id });
  }

  createComment(postId: Number, body: String): Observable<any>{
    return this.http.post<any>(this.baseUrl + '/feed/v1/comments/create', {post_id: postId, body: body})
  }

  createPost(post: Post){
    return this.http.post<any>(this.baseUrl + "/feed/v1/create", {
      title: post.title,
      body: post.body,
      group_id: this.userService.id
    })
  }

}
