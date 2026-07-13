import { login_user } from "../api/api"
import { useState } from "react"


export default function LoginPage(){
    const [username,setUsername] = useState("")
    const [password,setPassword] = useState("")

   

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data ={
            "username": username,
            "password":password
        }

        const response = await login_user(data)
        localStorage.setItem("access_token",response.access_token)

    }


    return(
        <div>
            <form onSubmit={handleSubmit}>

                <div>
                    <label htmlFor="username">Username: </label>
                    <input type="text" id="username" required onChange={(e) => setUsername(e.target.value)}/>
                </div>


                <div>
                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" required onChange={(e) => setPassword(e.target.value)}/>
                </div>

                
                <button type="submit">Log In</button>

            </form>
        </div>
    )
}