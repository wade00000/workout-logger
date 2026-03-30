import App from "./App"
import RegisterPage from "./pages/RegisterPage"

const routes = [
    {
        path:"/",
        element:<App/>,
        children: [
            {
                path:"/register",
                element:<RegisterPage/>
            }
        ]

    }
]

export default routes
