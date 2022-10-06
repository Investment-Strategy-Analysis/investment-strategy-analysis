import styles from './RiskTile.css';
import Tile from "../Tile/Tile";

function RiskTile() {
    return (
        <Tile>
            <div class="risk">
                <label for="riskRange" class="form-label">Risk</label>
                <input type="range" class="form-range" id="riskRange"/>

                <label for="profitRange" class="form-label">Profit</label>
                <input type="range" class="form-range" id="profitRange"/>
            </div>
        </Tile>
    );
}

export default RiskTile;
