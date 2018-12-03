import { Injectable } from '@angular/core';
import { User } from "../models/user"
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  private user: User; 

  setUser(user: User){
    this.user = user;
    console.log(this.user);
  }

  getId(): Number{
    return this.user.id;
  }

  getUser(): User{
    return this.user;
  }

  getUserObservable(): User{
    return this.user;
  }

  userIsSet(): Boolean{
    return this.user === null;
  }

  isFriend(id: Number): Boolean{
    var friend = this.user.friends.find(friend => friend.id === id);
    return this.user.friends.includes(friend);
  }
}
