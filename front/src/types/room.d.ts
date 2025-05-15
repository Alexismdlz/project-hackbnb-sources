import type { User } from "./user";

export type Room = {
    id: string;
    title: string;
    city: string;
    price: number;
    picture: string;
    description: string;
    host?: User;
}
