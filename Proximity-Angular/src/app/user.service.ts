import { Injectable } from '@angular/core';
import { User } from "./models/user"

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  user: User; 

  setUser(user: User){
    this.user = user;
  }

  getId(): Number{
    if(this.user){
      return this.user.getId();
    }
    return -1;
  }

  getUser(): User{
    return this.user;
  }

  userIsSet(): Boolean{
    return this.user === null;
  }
}
