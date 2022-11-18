import styles from './StrategyTile.module.css';
import Tile from "../Tile/Tile";
import {checkboxSettings, setStrategy, strategy, strategyOption, timeSettings} from "../../js/settings";
import {createEffect, For} from "solid-js";

function StrategyTile() {

    function handleStrategyOptionClick(event) {
        let option = event.currentTarget.value;
        let strategyData = strategyOption().filter(it => it.id === option)[0];

        setStrategy(strategyData);
    }

    createEffect(() => {
        timeSettings().forEach((it) => it.checked = false);
        timeSettings()
            .filter((it) => it.id === strategy().time_period)
            .forEach((it) => {
                it.checked = true;
                document.getElementById(it.id).checked = true;
            });
    })

    createEffect(() => {
        checkboxSettings().forEach((it) => {
            it.checked = strategy().checkboxes.some((checkbox) => it.id === checkbox);
            document.getElementById(it.id).checked = it.checked;
        })
    })

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
