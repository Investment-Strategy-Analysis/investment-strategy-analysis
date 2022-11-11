import styles from './StrategyTile.module.css';
import Tile from "../Tile/Tile";
import {setStrategy, strategy, strategyOption} from "../../js/web_constants";
import {For} from "solid-js";

function StrategyTile() {

    function handleStrategyOptionClick(event) {
        let option = event.currentTarget.value;
        let strategyData = strategyOption().filter(it => it.id === option)[0];

        setStrategy(strategyData);
    }

    return (
        <Tile>
            <h5>Strategy</h5>
            <div class={styles.strategy}>
                <div class={styles.strategySelector}>
                    <select class="form-select" id="strategyOptionSelector" onChange={handleStrategyOptionClick}>
                        <For each={strategyOption()}>{(option, _) =>
                            <option value={option.id}> {option.name} </option>
                        }</For>
                    </select>
                </div>
                <div> {strategy().description} </div>
            </div>
        </Tile>
    );
}

export default StrategyTile;
