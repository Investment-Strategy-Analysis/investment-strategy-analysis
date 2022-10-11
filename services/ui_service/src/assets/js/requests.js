const SERVER = "http://localhost:8000";
let TOKEN = null;

async function login() {
	const login = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const options = {
        method: "POST",
        body: JSON.stringify({ "username": login, "password": password }),
        headers: {
            "Content-Type": "application/json"
        }
    }
    const response = await fetch(
        `${SERVER}/login`,
        options,
    );
    console.log("Execution response: ", response);

    if (response.ok) {
        TOKEN = await response.json();
        console.log(TOKEN);
    }
}

async function signup() {
    const login = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const options = {
        method: "POST",
        body: JSON.stringify({ "username": login, "password": password }),
        headers: {
            "Content-Type": "application/json"
        }
    }
    const response = await fetch(
        `${SERVER}/signup`,
        options,
    );
    console.log("Execution response: ", response);

    if (response.ok) {
        console.log("OK");
    }
}
