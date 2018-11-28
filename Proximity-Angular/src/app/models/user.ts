import { Friend } from "./friend";
export class User extends Friend{
    constructor(id: Number, name: String, friends: Array<Friend>){
        super(name, id);
        this.friends = friends;
    } 

    private friends: Array<Friend>;

    getFriends(): Array<Friend>{
        return this.friends;
    }

    addFriend(friend: Friend){
        this.friends.concat(friend);
    }
}