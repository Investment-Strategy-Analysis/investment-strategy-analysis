import styles from './ResultTile.css';
import Tile from "../Tile/Tile";
import {createSignal, Match, Switch} from "solid-js";

const [results, setResults] = createSignal([]);

export function ResultTile() {
    return (
        <Tile>
            <h5>The best configuration</h5>

            <Switch fallback={<i>empty now</i>}>
                <Match when={results().length > 0} keyed>
                    <For each={results()}>{(name, value) =>
                        <div class="row">
                            <div class="col-6">
                                {name}
                            </div>
                            <div class="col-6">
                                {value}
                            </div>
                        </div>
                    }</For>
                </Match>
            </Switch>
        </Tile>
    );
}

export {setResults}
