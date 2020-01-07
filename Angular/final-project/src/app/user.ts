export class User {
    name: string;
    email: string;
    password: string;
    password_confirmation: string;
    token?:string;
    user: {
        id?: number;
        name?: string;
        email?: string;
        created_at?:Date;
        updated?: Date;
    }
}