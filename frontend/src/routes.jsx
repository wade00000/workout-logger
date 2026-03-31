import App from "./App"
import RegisterPage from "./pages/RegisterPage"
import LoginPage from "./pages/LoginPage"
import ProtectedRoutes from "./utils/ProtectedRoutes"
import HomePage from "./pages/HomePage"
import LandingPage from "./pages/LandingPage"

const routes = [
    {
        path:"/",
        element:<App/>,
        children: [
            {
                path:"/register",
                element:<RegisterPage/>
            },
            {
                path:"/login",
                element:<LoginPage/>
            },
            {
                path:"/landing",
                element: <LandingPage/>
            },
            {
                element: <ProtectedRoutes/>,
                children: [
                    { index: true , element: <HomePage/> },
                ]
            }
        ]

    }
]

export default routes
