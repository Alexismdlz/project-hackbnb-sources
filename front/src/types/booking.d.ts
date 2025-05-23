import type { Room } from "./room";
import type { User } from "./user";

export type Booking = {
    id: string;
    reference: string;
    arrival_date: string;
    departure_date: string;
    guests_count: number;
    total_price: number;
    is_paid: boolean;
    room: Room;
    stripe_checkout_session_id: string;
}
