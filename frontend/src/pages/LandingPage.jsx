import React from 'react';
import { Link } from 'react-router';

function LandingPage() {
    return (
        <div>
            <h1>Landing Page</h1>
            <Link to={"/login"}>Login</Link>
            <Link to={"/register"}>Sign Up</Link>
        </div>
    );
}

export default LandingPage;