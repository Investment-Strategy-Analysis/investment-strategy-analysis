import Cookies from 'js-cookie';
import {USER_SERVER} from "./web_constants";

/**
 * Check access token. If cookies does not contain token, or it is overdue redirect to login page.
 * @return {Promise<boolean>}
 */
export async function checkToken() {
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
    const status = (await fetch(
        `${USER_SERVER}/user`,
        options,
    )).status;

    if (status === 400 || status === 401 || status === 403) {
        window.location.replace(`/auth/login/`);
    }

    return true;

}

/**
 * Request to login and save tokens to cookies.
 * @param {string} username
 * @param {string} password
 * @return {Promise<Response>}
 */
export async function login(username, password) {
    const details = {
        "grant_type": "",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": ""
    };

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

    if (response.ok) {
        let data = await response.json();
        Cookies.set('ACCESS_TOKEN', data['access_token']);
        Cookies.set('REFRESH_TOKEN', data['refresh_token']);
    }
    return response;
}

/**
 * Request to sign up.
 * @param {string} username
 * @param {string} password
 * @return {Promise<Response>}
 */
export async function signup(username, password) {
    const options = {
        method: "POST",
        body: JSON.stringify({ "login": username, "password": password }),
        headers: {
            "Content-Type": "application/json"
        }
    }
    const response = await fetch(
        `${USER_SERVER}/user`,
        options,
    );

    return response;
}
