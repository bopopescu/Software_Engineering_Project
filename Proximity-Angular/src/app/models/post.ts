import { Comment } from './comment';

// export class Post{
//     constructor(title: String, body: String, comments: Array<Comment>){
//         this.title = title,
//         this.body = body,
//         this.comments = comments;
//     }

//     title: String
//     body: String
//     creator: String
//     comments: Array<Comment>

//     setTitle(title: String){
//         this.title = title;
//     }

//     setBody(body: String){
//         this.body = body;
//     }
// }

export interface Post{
    title: String
    body: String
    name: String
    time?: DateConstructor
    comments?: Array<Comment>
    displayComments: Boolean
}