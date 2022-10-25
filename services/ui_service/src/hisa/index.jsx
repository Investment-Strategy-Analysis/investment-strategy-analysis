/* @refresh reload */
import {render} from 'solid-js/web';

import styles from './hisa.module.css';
import NavBar from "../components/NavBar/NavBar";
import {splitProps} from "solid-js";

function Button(props) {
    const [local, _] = splitProps(props, ['title', 'url', 'background']);

    let onClick = () => window.location.replace(local.url);

    return (
        <div class={styles.linkbutton} style={{"background-color": local.background}}>
            <button type="button" class="btn btn-link" onClick={onClick}>{local.title}</button>
        </div>
    );
}

function Hisa() {
    let tryBackground = "#91E7ECFF";
    let signupBackground = "#64BCD9FF";
    let loginBackground = "#d5d5d5";
    return (
        <>
            <NavBar/>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <h1 class={styles.hisatitle}>Historical<br/>
                        Investment Strategy<br/>
                        Analysis
                    </h1>
                </div>
                <div class="row mb-2 ms-2 me-2">
                    <div class="col-lg-3"/>
                    <div class="col-lg-2 ">
                        <Button title="Try now" url="/analyzer/" background={tryBackground}/>
                    </div>
                    <div class="col-lg-2">
                        <Button title="Sign up" url="/auth/signup/" background={signupBackground}/>
                    </div>
                    <div class="col-lg-2">
                        <Button title="Log in" url="/auth/login/" background={loginBackground}/>
                    </div>
                </div>
                <div class="row mb-2 ms-2 me-2">
                    <div class={styles.titleGraphicDiv}>
                        <img class={styles.titleGraphic} src="../assets/imgs/graphic.png" alt="Profit-risk graphic"/>
                    </div>
                </div>
            </div>
        </>
    );
}

render(() => <Hisa/>, document.getElementById('root'));
