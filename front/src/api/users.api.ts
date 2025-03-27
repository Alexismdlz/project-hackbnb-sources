import axios from "axios";

/**
 * Get current user details from API
 */
export const apiCurrentUserDetails = () => {
    return axios.get(`/users/me`)
}
