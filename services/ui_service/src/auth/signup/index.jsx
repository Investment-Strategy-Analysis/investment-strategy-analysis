/* @refresh reload */
import { render } from 'solid-js/web';

import './sign_up_style.css';
import AuthBlock from "../../components/AuthBlock/AuthBlock";
import NavBar from "../../components/NavBar/NavBar";
import {USER_SERVER} from "../../assets/js/constants";

function SignUp() {

    function setWrongPasswordStyle() {
        const passwordAgainTag = document.getElementById("password_again_field");
        passwordAgainTag.style["border-color"] = "#af0000";
    }

    function resetPasswordStyle() {
        const passwordAgainTag = document.getElementById("password_again_field");
        passwordAgainTag.style["border-color"] = "#d0d7de";
    }

    async function signup() {
        const login = document.getElementById("username_field").value;
        const password = document.getElementById("password_field").value;
        const passwordAgain = document.getElementById("password_again_field").value;

        if (password !== passwordAgain) {
            setWrongPasswordStyle();
            return;
        }
        const options = {
            method: "POST",
            body: JSON.stringify({ "login": login, "password": password }),
            headers: {
                "Content-Type": "application/json"
            }
        }
        const response = await fetch(
            `${USER_SERVER}/user`,
            options,
        );
        console.log("Execution response: ", response);

        if (response.ok) {
            console.log("OK");
            window.location.replace(`/auth/login/`)
        } else {
            alert(response.body)
        }
    }

    const title = "Sing Up to HISA"
    return (
        <>
            <NavBar/>
            <AuthBlock title={title}>
                <div class="auth-field-block">
                    <label for="username_field">Username</label>
                    <input type="text" name="username" class="form-control" id="username_field" placeholder="Username"
                           autofocus="autofocus"/>
                </div>
                <div class="auth-field-block">
                    <label for="floatingPassword">Password</label>
                    <input type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                </div>
                <div class="auth-field-block">
                    <label for="floatingPasswordAgain">Password again</label>
                    <input onkeypress={resetPasswordStyle} type="password" class="form-control" id="password_again_field" placeholder="Password again"/>
                </div>

                <button class="auth-button w-100 btn btn-primary" type="submit" onclick={signup}>Sign up</button>
            </AuthBlock>
        </>
    );
}

render(() => <SignUp />, document.getElementById('root'));
