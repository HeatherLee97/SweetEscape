
export interface SessionInitialState {
    user: null | User;
}

export interface IUser {
    id: number;
    email: string;
}

export interface ISignUpUser{
    email: string;
    username: string;
    password: string;
}


export interface ICredentials {
    credential?: string;
    email?: string;
    password: string;

}
