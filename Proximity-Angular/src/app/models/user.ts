import{ Post } from "./post"
export interface User{
    first_name: String
    last_name: String
    full_name: String
    id: Number
    email: String
    distance?: Number
    posts?: Array<Post>
    friends?: Array<User>
    events?: Array<Event>
}