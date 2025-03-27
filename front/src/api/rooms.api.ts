import axios from "axios";

/**
 * List all available rooms from API with given category
 */
export const apiRoomsList = (category: string | null) => {
    return axios.get(category ? `/rooms/?category=${encodeURIComponent(category)}` : `/rooms/`)
}

/**
 * Get room details from API
 */
export const apiRoomDetails = (roomId: string) => {
    return axios.get(`/rooms/${encodeURIComponent(roomId)}`)
}
