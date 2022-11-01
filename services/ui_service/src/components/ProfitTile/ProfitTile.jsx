import styles from './ProfitTile.module.css';
import Tile from "../Tile/Tile";
import {createEffect, createSignal} from "solid-js";
import {initProfit, maxProfit, minProfit, stepProfit} from "../../js/web_constants";

function ProfitTile() {
    const [profit, setProfit] = createSignal(initProfit);
    const getRange = () => document.getElementById("profitRange");
    const getRangeNumber = () => document.getElementById("profitRangeNumber");

    createEffect(() => {
        getRange().value = profit();
        getRangeNumber().value = profit();
    })

    createEffect(() => {
            if (profit() > maxProfit) {
                setProfit(maxProfit);
            }
            if (profit() < minProfit) {
                setProfit(minProfit)
            }
        }
    )

    return (
        <Tile>
            <div class={styles.profit}>
                <label for="profitRange" class="form-label"><h5>Profit</h5></label>
                <span class={styles.profitValue}>
                    <div class="input-group">
                        <input type="number" class="form-control" id="profitRangeNumber" min={minProfit} max={maxProfit} step={stepProfit}
                               onChange={() => setProfit(getRangeNumber().value)}/>
                        <div class={styles.percentGroup}>
                            <span class="input-group-text">%</span>
                        </div>
                    </div>
                </span>
                <div class={styles.profitRange}>
                    <input type="range" class="form-range" id="profitRange" min={minProfit} max={maxProfit} step={stepProfit}
                           onChange={() => setProfit(getRange().value)}/>
                </div>
            </div>
        </Tile>
);
}

export default ProfitTile;
