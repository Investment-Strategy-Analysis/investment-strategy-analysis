import './SignUp.css';
import AuthBlock from "../../../components/AuthBlock/AuthBlock";
import {USER_SERVER} from "../../../js/web_constants";
import {signup} from "../../../js/authorization";
import {useRoutes} from "solid-app-router";

function SignUp() {

    function showInvalidMessage() {
        const passwordAgainTag = document.getElementById("errorMessage");
        passwordAgainTag.style["display"] = "block";
    }

    function setWrongPasswordStyle() {
        const passwordAgainTag = document.getElementById("password_again_field");
        passwordAgainTag.style["border-color"] = "#af0000";
    }

    function resetPasswordStyle() {
        const passwordAgainTag = document.getElementById("password_again_field");
        passwordAgainTag.style["border-color"] = "#d0d7de";
    }

    async function _signup() {
        const username = document.getElementById("username_field").value;
        const email = document.getElementById("email_field").value;
        const password = document.getElementById("password_field").value;
        const passwordAgain = document.getElementById("password_again_field").value;

        if (password !== passwordAgain) {
            setWrongPasswordStyle();
            return;
        }

        const response = await signup(username, password, email);

        if (response.ok) {
            window.location.replace(`/auth/login/`);
        } else {
            showInvalidMessage();
        }
    }

    const title = "Sign Up to HISA"
    return (
        <>
            <AuthBlock title={title}>
                <div class="error-message" id="errorMessage">
                    Incorrect username, email or password.
                </div>
                <div class="auth-field-block">
                    <label for="username_field">Username</label>
                    <input type="text" name="username" class="form-control" id="username_field" placeholder="Username"
                           autofocus="autofocus"/>
                </div>
                <div class="auth-field-block">
                    <label for="username_field">Email</label>
                    <input type="email" name="email" class="form-control" id="email_field" placeholder="user@email.com"
                           />
                </div>
                <div class="auth-field-block">
                    <label for="floatingPassword">Password</label>
                    <input type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                </div>
                <div class="auth-field-block">
                    <label for="floatingPasswordAgain">Password again</label>
                    <input onkeypress={resetPasswordStyle} type="password" class="form-control" id="password_again_field" placeholder="Password again"/>
                </div>

                <button class="auth-button w-100 btn btn-primary" type="submit" onclick={_signup}>Sign up</button>
            </AuthBlock>
        </>
    );
}

export default SignUp;