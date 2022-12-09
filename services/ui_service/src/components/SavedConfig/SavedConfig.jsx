import {createSignal, For} from "solid-js";
import Tile from "../Tile/Tile";
import styles from './SavedConfig.module.css';
import {USER_SERVER} from "../../js/web_constants";
import {formatFloatValue} from "../../js/utils";

const [configurations, setConfigurations] = createSignal([]);

async function loadConfigurations() {
    const access_token = Cookies.get('ACCESS_TOKEN');
    const options = {
        headers: {
            'accept': 'application/json',
            'Authorization': `Bearer ${access_token}`,
            "Content-Type": "application/json;charset=utf-8"
        }
    }
    const response = await fetch(
        `${USER_SERVER}/user/settings`,
        options
    );
    if (response.ok) {
        const settings = await response.json();
        setConfigurations(settings);
    }
}

async function selectConfiguration(config) {
    let body = config;

    const access_token = Cookies.get('ACCESS_TOKEN');
    const options = {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
            'accept': 'application/json',
            'Authorization': `Bearer ${access_token}`,
            "Content-Type": "application/json;charset=utf-8"
        }
    }
    await fetch(
        `${USER_SERVER}/user/current_settings`,
        options,
    );
}

function SavedConfig() {
    loadConfigurations().then((_) => console.log("OK"));
    return (
        <For each={configurations()}>{(c, _) =>
            <Tile>
                <div class={styles.tileContent}>
                    <div class={styles.description}>Strategy: {c.strategy}</div>
                    <div class={styles.description}>Profit: {c.restrictions.target_profit}</div>
                    <div class={styles.description}>Risk: {formatFloatValue(c.risk)}</div>

                    <div class={styles.openButton}>
                        <button type="button" class="btn btn-info btn-sm" onClick={() => {
                            selectConfiguration(c).then(r => {
                                console.log("OK");
                                window.location.replace(`/analyzer/`);
                            });
                        }
                        }>Open
                        </button>
                    </div>
                </div>
            </Tile>
        }</For>
    );
}

export default SavedConfig;