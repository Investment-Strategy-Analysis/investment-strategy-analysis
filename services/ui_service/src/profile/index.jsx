/* @refresh reload */
import { render } from 'solid-js/web';

import './profile.css';
import AuthBlock from "../components/AuthBlock/AuthBlock";
import NavBar from "../components/NavBar/NavBar";
import SavedConfig from "../components/SavedConfig/SavedConfig";
import {USER_SERVER} from "../assets/js/constants";

function Profile() {
    function login() {
        const access_token = Cookies.get('ACCESS_TOKEN');
        if (access_token === undefined) {
            window.location.replace(`/auth/login/`);
        }
        // Cookies.set('REFRESH_TOKEN', data['refresh_token']);

        const options = {
            method: "GET",
            headers: {
                'accept': 'application/json',
                'Authorization': `Bearer ${access_token}`
            }
        };
        const response = fetch(
            `${USER_SERVER}/user`,
            options,
        );
        response.then(resp => {
            if (resp.status === 401 || resp.status === 403) {
                window.location.replace(`/auth/login/`);
            }
        });
    }

    function setWrongPasswordStyle() {
        const passwordAgainTag = document.getElementById("password_again_field");
        passwordAgainTag.style["border-color"] = "#af0000";
    }

    async function save() {
        const login = document.getElementById("username_field").value;
        const password = document.getElementById("password_field").value;
        const passwordAgain = document.getElementById("password_again_field").value;

        if (password !== passwordAgain) {
            setWrongPasswordStyle();
            return;
        }
        const data = {};
        if (login !== undefined) {
            data["login"] = login;
        }
        if (password !== undefined) {
            data["password"] = password;
        }

        const options = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        }
        // Todo: add api for profile updating
    }

    login();

    return (
        <>
            <NavBar/>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <div class="col-md-8">
                        <h3 class="title">Your configurations</h3>
                        <SavedConfig/>
                    </div>
                    <div class="col-md-4">
                        <h5 class="title">Change Username or Password</h5>
                        <div class="auth-field-block">
                            <label for="username_field">Username</label>
                            <input type="text" name="username" class="form-control" id="username_field" placeholder="Username"/>
                        </div>
                        <div class="auth-field-block">
                            <label for="floatingPassword">Password</label>
                            <input type="password" name="password" class="form-control" id="password_field" placeholder="Password"/>
                        </div>
                        <div class="auth-field-block">
                            <label for="floatingPasswordAgain">Password again</label>
                            <input type="password" class="form-control" id="password_again_field" placeholder="Password again"/>
                        </div>

                        <button class="auth-button w-100 btn btn-primary" type="submit" onClick={save}>Save</button>
                    </div>
                </div>
            </div>
        </>
    );
}

render(() => <Profile />, document.getElementById('root'));
