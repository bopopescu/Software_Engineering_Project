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
export interface User{
    firstName: String
    lastName: String
    id: Number
    email: String
    latitude?: Number
    longitude?: Number
    posts?: Array<Post>
    friends?: Array<User>
}