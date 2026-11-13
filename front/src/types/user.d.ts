export type User = {
    id: string;
    name: string;
    email?: string; // renvoyé seulement par /users/me
}
