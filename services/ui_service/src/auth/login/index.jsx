/* @refresh reload */
import { render } from 'solid-js/web';

import './log_in_style.css';
import AuthBlock from "../../components/AuthBlock/AuthBlock";
import NavBar from "../../components/NavBar/NavBar";
import '../../assets/js/requests';

function SignUp() {
    const title = "Log In to HISA"
    return (
        <>
            <NavBar/>
            <AuthBlock title={title}>
                {/*<form action="">*/}
                    <div class="auth-field-block">
                        <label for="username_field">Username</label>
                        <input type="text" name="username" class="form-control" id="username_field" placeholder="Username"
                               autofocus="autofocus"/>
                    </div>
                    <div class="auth-field-block">
                        <label for="floatingPassword">Password</label>
                        <input type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                    </div>

                    <button class="auth-button w-100 btn btn-primary" type="submit" onclick="login()">Log in</button>
                {/*</form>*/}
            </AuthBlock>
            <p class="mt-3 create-account">
                Do not have account?  <a href="/auth/signup/">Create it!</a>
            </p>
        </>
    );
}

render(() => <SignUp />, document.getElementById('root'));
