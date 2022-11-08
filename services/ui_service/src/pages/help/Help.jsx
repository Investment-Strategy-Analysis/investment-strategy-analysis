import styles from './Help.module.css';

function Help() {
    return (
        <>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <h1 class={styles.MainTitle}>
                        Help
                    </h1>
                    <h4 class={styles.Comment}>This page is being developed. Information about our project will be here...</h4>
                </div>
            </div>
        </>
    );
}

export default Help;