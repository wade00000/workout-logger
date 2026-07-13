import { React,useState,useEffect } from 'react';
import { get_user } from '../api/api';
import { Link } from 'react-router';

function HomePage() {
    const [user,setUser] = useState("")

    
    const load_curr_user = async () => {
        const response = await get_user()
        setUser(response)
    }

    const handleLogOut = () => {
        localStorage.removeItem("access_token")
    }


    useEffect(()=>{
        load_curr_user()
    },[])
    
    return (
        <div>
            <Link to={"/landing"} onClick={handleLogOut}>Log Out</Link>
            <h1>Home Page</h1>
            <h2>Welcome {user.username}</h2>
            <h3>Email: {user.email}</h3>
        </div>
    );
}

export default HomePage;