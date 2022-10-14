import styles from './AuthBlock.css';
import {children} from "solid-js";

function AuthBlock(props) {
    const c = children(() => props.children);
    return (
        <>
            <div class="pt-5 auth-form">
                <h1 class="auth-from-title h3 mb-4">{props.title}</h1>
                <div class="auth-form-body">
                    {c()}
                </div>
            </div>
        </>
    );
}

export default AuthBlock;
