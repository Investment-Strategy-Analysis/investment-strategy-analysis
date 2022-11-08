import {lazy} from 'solid-js';
import {Router, useRoutes} from "solid-app-router";

import NavBar from "./components/NavBar/NavBar.jsx";
import {render} from "solid-js/web";
import {checkToken} from "./js/authorization";

const routes = [
    {
        path: '/',
        component: lazy(() => import('./pages/hisa/Hisa'))
    },
    {
        path: '/help',
        component: lazy(() => import('./pages/help/Help'))
    },
    {
        path: '/analyzer',
        component: lazy(() => import('./pages/analyzer/Analyzer'))
    },
    {
        path: '/profile',
        component: lazy(() => checkToken().then(res => import('./pages/profile/Profile')))
    },
    {
        path: '/auth/login',
        component: lazy(() => import('./pages/auth/login/LogIn'))
    },
    {
        path: '/auth/signup',
        component: lazy(() => import('./pages/auth/signup/SignUp'))
    },
];

function App() {
    const Routes = useRoutes(routes);
    return (
        <>
            <NavBar/>
            <Routes/>
        </>
    );
}

render(
    () => (
        <Router>
            <App/>
        </Router>
    ),
    document.getElementById("root")
);
