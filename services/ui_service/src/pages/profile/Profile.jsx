import './Profile.css';
import SavedConfig from "../../components/SavedConfig/SavedConfig";
import {createSignal} from "solid-js";
import {USER_SERVER} from "../../js/web_constants";

const [username, setUsername] = createSignal("hisa");
const [email, setEmail] = createSignal("hisa@yandex.ru");

async function loadProfile() {
    const access_token = Cookies.get('ACCESS_TOKEN');
    const options = {
        headers: {
            'accept': 'application/json',
            'Authorization': `Bearer ${access_token}`,
            "Content-Type": "application/json;charset=utf-8"
        }
    }
    const response = await fetch(
        `${USER_SERVER}/user`,
        options
    );
    if (response.ok) {
        let userData = await response.json();
        setUsername(userData.login);
        setEmail(userData.user_settings.email);
    }
}

function Profile() {
    loadProfile().then((_) => console.log("OK"));

    return (
        <>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <div class="col-md-4">
                        <img src="/assets/imgs/user-icon.png" class="user-photo" alt="Icon"/>
                    </div>
                    <div class="col-md-8 profile-info">
                        <div class="row">
                            <h3>
                                Username
                            </h3>
                            <p>
                                {username()}
                            </p>
                        </div>
                        <div class="row">
                            <h3>
                                Email
                            </h3>
                            <p>
                                {email()}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="row mb-2 ms-2 me-2">
                    <h1 class="title">Your configurations</h1>
                    <SavedConfig/>
                </div>
            </div>
        </>
    );
}

export default Profile;