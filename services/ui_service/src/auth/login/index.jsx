/* @refresh reload */
import { render } from 'solid-js/web';

import Cookies from 'js-cookie'
import './log_in_style.css';
import AuthBlock from "../../components/AuthBlock/AuthBlock";
import NavBar from "../../components/NavBar/NavBar";
import {USER_SERVER} from "../../assets/js/constants";

function LogIn() {

    function showInvalidLogin() {
        const passwordAgainTag = document.getElementById("errorMessage");
        passwordAgainTag.style["display"] = "block";
    }

    function resetInvalidLogin() {
        const passwordAgainTag = document.getElementById("errorMessage");
        passwordAgainTag.style["display"] = "none";
    }

    async function login() {
        const login = document.getElementById("username_field").value;
        const password = document.getElementById("password_field").value;
        const details = {
            "grant_type": "",
            "username": login,
            "password": password,
            "scope": "",
            "client_id": "",
            "client_secret": ""
        };
        console.log(details);

        let formBody = [];
        for (let property in details) {
            let encodedKey = encodeURIComponent(property);
            let encodedValue = encodeURIComponent(details[property]);
            formBody.push(encodedKey + "=" + encodedValue);
        }
        formBody = formBody.join("&");

        const options = {
            method: "POST",
            body: formBody,
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
        const response = await fetch(
            `${USER_SERVER}/login`,
            options,
        );
        console.log("Execution response: ", response);

        if (response.ok) {
            let data = await response.json();
            Cookies.set('ACCESS_TOKEN', data['access_token']);
            Cookies.set('REFRESH_TOKEN', data['refresh_token']);
            window.location.replace(`/analyzer/`)
        } else {
            showInvalidLogin();
        }
    }

    const title = "Log In to HISA"
    return (
        <>
            <NavBar/>
            <AuthBlock title={title}>
                <div class="error-message" id="errorMessage">
                    Incorrect username or password.
                </div>
                <div class="auth-field-block">
                    <label for="username_field">Username</label>
                    <input onkeypress={resetInvalidLogin} type="text" name="username" class="form-control" id="username_field" placeholder="Username"
                           autofocus="autofocus"/>
                </div>
                <div class="auth-field-block">
                    <label for="floatingPassword">Password</label>
                    <input onkeypress={resetInvalidLogin} type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                </div>

                <button class="auth-button w-100 btn btn-primary" type="submit" onClick={login}>Log in</button>
            </AuthBlock>
            <p class="mt-3 create-account">
                Do not have account?  <a href="/auth/signup/">Create it!</a>
            </p>
        </>
    );
}

render(() => <LogIn />, document.getElementById('root'));
