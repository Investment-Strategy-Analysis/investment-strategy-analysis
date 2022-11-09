import styles from './Help.module.css';

function Help() {
    return (
        <>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <h1 class={styles.MainTitle} id="HISA-Help">HISA Help</h1>
                    <p>
                        Our application will help you to choose the best investment strategy based on your desired
                        income level and your willingness to take risks.
                    </p>
                    <ul>
                        <li>The title page is available <a href="/">here</a>. You can also get
                            to it by clicking on the <strong>HISA</strong> logo
                            on the left corner.
                        </li>
                        <li>If you do not have an account, please, click the <strong>Sign up</strong> button on the
                            title page or follow the <a href="/auth/signup/">link</a> to create
                            one.
                        </li>
                        <li>If you already have an account, click the <strong>Log in</strong> button on the title page
                            or follow the <a href="/auth/login/">link</a>.
                        </li>
                        <li>After log in, you will get to the HISA main page. Here you can choose the appropriate
                            investment settings like types of stocks and bonds, investment period, desired profit and
                            acceptable risk. When these parameters are chosen, the program will find an optimal
                            investment strategy for you, showing a risk/profit graph.
                        </li>
                        <li>All found configurations will be saved in your personal account. Three last configurations
                            are stored free of charge. If you
                            want to store more, you should pay for it.
                        </li>
                        <li>You can get to your personal account by clicking on the <strong>User</strong> icon on the
                            right corner.
                        </li>
                        <li>The main page is also available by clicking the <strong>Analyzer</strong> button.</li>
                        <li>You can use HISA without creating an account (click <strong>Analyzer</strong> or <strong>Try
                            now</strong> on the title page), but neither of your configurations will be saved in this
                            case.
                        </li>
                    </ul>
                </div>
            </div>
        </>
    );
}

export default Help;