import styles from './ResultTile.css';
import Tile from "../Tile/Tile";
import {createSignal, Match, Switch} from "solid-js";
import {formatFloatValue} from "../../js/utils";

const [results, setResults] = createSignal([]);

export function ResultTile() {
    return (
        <Tile>
            <h5>The best configuration</h5>

            <Switch fallback={<i>empty now</i>}>
                <Match when={results().length > 0} keyed>
                    <For each={results()}>{res =>
                        <div class="row">
                            <div class="col-8">
                                {res[0]}
                            </div>
                            <div class="col-4">
                                {formatFloatValue(res[1])}
                            </div>
                        </div>
                    }</For>
                </Match>
            </Switch>
        </Tile>
    );
}

export {setResults}
