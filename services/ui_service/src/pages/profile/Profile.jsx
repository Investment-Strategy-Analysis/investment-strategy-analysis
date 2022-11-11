import './Profile.css';
import SavedConfig from "../../components/SavedConfig/SavedConfig";

function Profile() {

    return (
        <>
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

                        <button class="auth-button w-100 btn btn-primary" type="submit">Save</button>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Profile;