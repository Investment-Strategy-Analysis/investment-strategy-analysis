import './Profile.css';
import SavedConfig from "../../components/SavedConfig/SavedConfig";
import {createSignal} from "solid-js";

const [username, setUsername] = createSignal("Username");
const [email, seEmail] = createSignal("username@email.com");

function Profile() {

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
                        {/*<div class="row">*/}
                        {/*    <button type="button" class="btn btn-outline-secondary" onClick={() => window.location.replace('/auth/change_password?next=/profile')}>Change Password</button>*/}
                        {/*</div>*/}
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