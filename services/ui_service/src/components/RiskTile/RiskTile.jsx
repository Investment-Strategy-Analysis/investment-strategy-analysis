import styles from './RiskTile.css';
import Tile from "../Tile/Tile";

function RiskTile() {
    return (
        <Tile>
            <div class={styles.risk}>
                <label for="riskRange" class="form-label"><h5>Risk</h5></label>
                <input type="range" class="form-range" id="riskRange"/>
            </div>
        </Tile>
    );
}

export default RiskTile;
