const SERVER = "http://localhost:8000";
let ACCESS_TOKEN = null;
let REFRESH_TOKEN = null;

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
        `${SERVER}/login`,
        options,
    );
    console.log("Execution response: ", response);

    if (response.ok) {
        let data = await response.json();
        ACCESS_TOKEN = data['access_token'];
        REFRESH_TOKEN = data['refresh_token']
        window.location.replace(`/analyzer/`)
    }
}

async function signup() {
    const login = document.getElementById("username_field").value;
    const password = document.getElementById("password_field").value;
    console.log(login, password)
    const options = {
        method: "POST",
        body: JSON.stringify({ "login": login, "password": password }),
        headers: {
            "Content-Type": "application/json"
        }
    }
    const response = await fetch(
        `${SERVER}/user`,
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
