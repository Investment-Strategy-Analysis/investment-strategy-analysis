import styles from './NotFound.module.css';

function NotFound() {
    return (
        <>
            <div class="container-lg">
                <div class="row mb-2 ms-2 me-2">
                    <h1 class={styles.Title404}>404 Not Found</h1>
                </div>
            </div>
        </>
    );
}

export default NotFound;