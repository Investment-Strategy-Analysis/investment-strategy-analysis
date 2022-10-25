import styles from './AuthBlock.css';
import {children, splitProps} from "solid-js";

function AuthBlock(props) {
    const [local, _] = splitProps(props, ['boxid', 'name']);
    const c = children(() => props.children);
    return (
        <>
            <div class="pt-5 auth-form">
                <h1 class="auth-from-title h3 mb-4">{local.title}</h1>
                <div class="auth-form-body">
                    {c()}
                </div>
            </div>
        </>
    );
}

export default AuthBlock;
