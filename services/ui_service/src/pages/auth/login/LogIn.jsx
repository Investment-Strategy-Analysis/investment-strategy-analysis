import Cookies from 'js-cookie';
import './LogIn.css';
import AuthBlock from "../../../components/AuthBlock/AuthBlock";
import {login} from "../../../js/authorization";

function LogIn() {

    function showInvalidMessage() {
        const passwordAgainTag = document.getElementById("errorMessage");
        passwordAgainTag.style["display"] = "block";
    }

    function resetInvalidMessage() {
        const passwordAgainTag = document.getElementById("errorMessage");
        passwordAgainTag.style["display"] = "none";
    }

    async function _login() {
        const username = document.getElementById("username_field").value;
        const password = document.getElementById("password_field").value;

        const response = await login(username, password);

        if (response.ok) {
            window.location.replace(`/analyzer/`);
        } else {
            showInvalidMessage();
        }
    }

    const title = "Log In to HISA"
    return (
        <>
            <AuthBlock title={title}>
                <div class="error-message" id="errorMessage">
                    Incorrect username or password.
                </div>
                <div class="auth-field-block">
                    <label for="username_field">Username</label>
                    <input onkeypress={resetInvalidMessage} type="text" name="username" class="form-control" id="username_field" placeholder="Username"
                           autofocus="autofocus"/>
                </div>
                <div class="auth-field-block">
                    <label for="floatingPassword">Password</label>
                    <input onkeypress={resetInvalidMessage} type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                </div>

                <button class="auth-button w-100 btn btn-primary" type="submit" onClick={_login}>Log in</button>
            </AuthBlock>
            <p class="mt-3 create-account">
                Do not have account?  <a href="/auth/signup">Create it!</a>
            </p>
        </>
    );
}

export default LogIn;
