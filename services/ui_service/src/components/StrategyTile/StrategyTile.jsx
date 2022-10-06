import styles from './StrategyTile.css';
import Tile from "../Tile/Tile";

function StrategyTile() {
    return (
        <Tile>
            <div class="strategy">
                <ul class="nav nav-tabs">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" data-bs-toggle="dropdown" href="#" role="button"
                           aria-expanded="false" style="">Default</a>
                        <ul class="dropdown-menu" style="">
                            <li><a class="dropdown-item" href="#">Risky</a></li>
                            <li><a class="dropdown-item" href="#">Safety</a></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                            <li>
                                <hr class="dropdown-divider"/>
                            </li>
                            <li><a class="dropdown-item" href="#">Default</a></li>
                        </ul>
                    </li>
                </ul>
                <div> Some text </div>
            </div>
        </Tile>
    );
}

export default StrategyTile;
