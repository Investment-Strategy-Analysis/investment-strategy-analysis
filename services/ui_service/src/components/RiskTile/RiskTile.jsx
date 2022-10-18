import styles from './RiskTile.css';
import Tile from "../Tile/Tile";

function RiskTile() {
    return (
        <Tile>
            <div class={styles.profit}>
                <label for="riskRange" class="form-label"><h5>Profit</h5></label>
                <input type="range" class="form-range" id="profitRange"/>
            </div>
        </Tile>
    );
}

export default RiskTile;
