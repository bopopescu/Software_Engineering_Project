import { Injectable } from '@angular/core';
import { User } from "../models/user"
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  setUser(user: User){
    localStorage.setItem('user', JSON.stringify(user));
    console.log("User set");
  }

  get id(): Number{
    return JSON.parse(localStorage.getItem('user')).id;
  }

  getUser(): User{
    return JSON.parse(localStorage.getItem('user')).user;
  }

  // getUserObservable(): User{
  //   return this.user;
  // }

  userIsSet(): Boolean{
    return JSON.parse(localStorage.getItem('user')) === null;
  }

  isFriend(id: Number): Boolean{
    var friend = JSON.parse(localStorage.getItem('user')).friends.find(friend => friend.id === id);
    return JSON.parse(localStorage.getItem('user')).friends.includes(friend);
  }
}
