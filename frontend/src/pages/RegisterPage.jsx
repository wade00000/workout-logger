import { useState } from "react"
import { register_user } from "../api/api"


export default function RegisterPage(){
    const [username,setUsername] = useState("")
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data ={
            "username": username,
            "email":email,
            "password":password
        }

        await register_user(data)

    }
    return(
        <div>
            <form onSubmit={handleSubmit}>

                <div>
                    <label htmlFor="username">Username: </label>
                    <input type="text" id="username" required onChange={(e) => setUsername(e.target.value)}/>
                </div>


                <div>
                    <label htmlFor="email">Email: </label>
                    <input type="email" id="email" required onChange={(e) => setEmail(e.target.value)} />
                </div>


                <div>
                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" required onChange={(e) => setPassword(e.target.value)}/>
                </div>

                <button type="submit">Sign Up</button>

            </form>
        </div>
    )
}