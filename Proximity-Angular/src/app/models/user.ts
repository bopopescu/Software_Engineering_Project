// import { Friend } from "./friend";
// export class User extends Friend{
//     constructor(id: Number, firstName: String, lastName: String, friends: Array<Friend>, ){
//         super(firstName, lastName, id);
//         this.friends = friends;
//     } 

//     private friends: Array<Friend>;

//     getFriends(): Array<Friend>{
//         return this.friends;
//     }

//     addFriend(friend: Friend){
//         this.friends.concat(friend);
//     }
// }
import{ Post } from "./post"
import { Location } from "./location"
export interface User{
    firstName: String
    lastName: String
    fullName: String
    id: Number
    email: String
    distance?: Number
    posts?: Array<Post>
    friends?: Array<User>
    events?: Array<Event>
}