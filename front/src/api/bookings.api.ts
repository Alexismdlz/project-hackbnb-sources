import axios from "axios";

/**
 * Get booking details from API
 */
export const apiBookingDetails = (bookingReference: string) => {
    return axios.get(`/bookings/${encodeURIComponent(bookingReference)}`)
}

/**
 * Get booking checkout lines from API
 */
export const apiBookingCheckoutLines = (bookingReference: string, checkoutSessionId: string) => {
    return axios.get(`/bookings/${encodeURIComponent(bookingReference)}/checkout-lines?checkout_session_id=${encodeURIComponent(checkoutSessionId)}`)
}

/**
 * Register a new booking
 */
export const apiBookingNew = (roomId: string, arrivalDate: string, departureDate: string, guestsCount: number) => {
    return axios.post(`/bookings/`, { roomId, arrivalDate, departureDate, guestsCount })
}

/**
 * Confirm checkout payment of a new booking
 */
export const apiBookingConfirm = (bookingReference: string, confirmationSecret: string) => {
    return axios.post(`/bookings/${bookingReference}/confirm-checkout`, { confirmationSecret })
}
