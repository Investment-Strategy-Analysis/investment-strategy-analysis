/* @refresh reload */
import { render } from 'solid-js/web';

import './sign_up_style.css';
import '../../assets/js/requests';
import AuthBlock from "../../components/AuthBlock/AuthBlock";
import NavBar from "../../components/NavBar/NavBar";

function SignUp() {
    const title = "Sing Up to HISA"
    return (
        <>
            <NavBar/>
            <AuthBlock title={title}>
                {/*<form>*/}
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
                        <input onkeypress="resetPasswordStyle()" type="password" class="form-control" id="password_again_field" placeholder="Password again"/>
                    </div>

                    <button class="auth-button w-100 btn btn-primary" type="submit" onclick="signup()">Sign up</button>
                {/*</form>*/}
            </AuthBlock>
        </>
    );
}

render(() => <SignUp />, document.getElementById('root'));