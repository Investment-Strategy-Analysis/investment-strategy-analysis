import styles from './ResultTile.css';
import Tile from "../Tile/Tile";
import {createSignal, Match, Switch} from "solid-js";
import {formatFloatValue} from "../../js/utils";
import {USER_SERVER} from "../../js/web_constants";

const [results, setResults] = createSignal([]);

export function ResultTile() {
    async function saveConfig() {
        const access_token = Cookies.get('ACCESS_TOKEN');
        const options = {
            method: "POST",
            headers: {
                'accept': 'application/json',
                'Authorization': `Bearer ${access_token}`,
                "Content-Type": "application/json;charset=utf-8"
            }
        }
        await fetch(
            `${USER_SERVER}/user/settings/add`,
            options,
        );
    }

    return (
        <Tile>
            <h5>The best configuration
                <div class="saveButton" onClick={() => saveConfig()}>
                    <i class="bi bi-save"></i>
                </div>
            </h5>

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
