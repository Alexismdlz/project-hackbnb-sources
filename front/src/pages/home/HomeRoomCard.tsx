import { NavLink } from "react-router-dom";
import type { Room } from "../../types/room";

/**
 * A card for single room result
 */
export const HomeRoomCard = ({ room }: { room: Room }) => {
    return <>
        <NavLink to={`/room/${room.id}`}>
            {/* Room Picture */}
            <div
                className="w-full aspect-square rounded-3xl bg-cover bg-center bg-no-repeat"
                style={{backgroundImage: `url('/api/uploads/?name=${encodeURIComponent(room.picture)}')`}}>
            </div>

            {/* Room Information */}
            <div className="mt-3 px-2">
                <div className="flex justify-between items-center">
                    <div className="font-medium">
                        {room.city}
                    </div>
                </div>

                <div className="text-gray-300">{room.title}</div>
                <div className="text-gray-300 mt-2">
                    <strong className="text-gray-100">{room.price} &euro;</strong> par nuit
                </div>
            </div>
        </NavLink>
    </>
}
