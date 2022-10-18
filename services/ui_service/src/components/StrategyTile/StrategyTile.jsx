import styles from './StrategyTile.module.css';
import Tile from "../Tile/Tile";

function StrategyTile() {
    return (
        <Tile>
            <h5>Strategy</h5>
            <div class={styles.strategy}>
                <div class={styles.strategySelector}>
                    <select class="form-select" aria-label="Default select example">
                        <option value="0" selected>Default</option>
                        <option value="1">Risky</option>
                        <option value="2">Safety</option>
                    </select>
                </div>
                <div> Some text about strategy </div>
            </div>
        </Tile>
    );
}

export default StrategyTile;
