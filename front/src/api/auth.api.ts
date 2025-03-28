import axios from "axios";

/**
 * Log in to the application
 */
export const apiAuthLogin = (email: string, password: string) => {
    return axios.post(`/auth/login`, { email, password })
}

/**
 * Create a new account in the application
 */
export const apiAuthRegister = (name: string, email: string, password: string) => {
    return axios.post(`/auth/register`, { name, email, password })
}
