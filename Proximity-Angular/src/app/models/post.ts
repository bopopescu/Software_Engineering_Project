export class Post{
    constructor(title: String, body: String){
        this.title = title,
        this.body = body
    }

    title: String
    body: String

    setTitle(title: String){
        this.title = title;
    }

    setBody(body: String){
        this.body = body;
    }
}