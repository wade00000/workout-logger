import { Outlet,Navigate } from "react-router"


const ProtectedRoutes = () => {
    const token = localStorage.getItem("access_token")
    return token ? <Outlet/> : <Navigate to="/landing"/>
}

export default ProtectedRoutes