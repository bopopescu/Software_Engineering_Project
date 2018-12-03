import { User } from "./user";

export interface Comment {
    body: String
    user: User
    time?: DateConstructor
}