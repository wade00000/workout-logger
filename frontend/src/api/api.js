import axios from "axios"

const BASE_URL = "http://127.0.0.1:5000"

export const register_user = async(data) =>{
    const response = await axios.post(`${BASE_URL}/users/register`,data)
    return response.data
}
export const login_user = async(data) =>{
    const response = await axios.post(`${BASE_URL}/users/login`,data)
    return response.data
    
}

export const get_user = async() => {
    const token = localStorage.getItem("access_token")
    const response = await axios.get(`${BASE_URL}/users/me`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
    return response.data

}
