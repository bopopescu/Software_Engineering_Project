import { Comment } from './comment';
import { User } from './user';

export interface Post{
    title: String
    body: String
    username: String
    time?: Number
    comments?: Array<Comment>
    displayComments?: Boolean
    isFriend?: Boolean
    // userId: Number
    id: Number
    distance: Number
    user: User
}