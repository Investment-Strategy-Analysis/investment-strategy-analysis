import styles from './NavBar.css';

function NavBar() {
    return (
        <nav class="navbar navbar-expand-md navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">
                    <img class="logo" src="/assets/imgs/hisa_logo.png" alt="HISA"/>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHISA"
                        aria-controls="navbarHISA" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarHISA">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/analyzer/">Analyzer</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/help/">Help</a>
                        </li>
                    </ul>
                    <a class="navbar-profile" href="/profile/">
                        <i class="bi bi-person-circle user-icon"></i>
                    </a>
                </div>
            </div>
        </nav>
    );
}

export default NavBar;
