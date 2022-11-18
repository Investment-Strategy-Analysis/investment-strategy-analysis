import {createSignal, For} from "solid-js";
import Tile from "../Tile/Tile";
import styles from './SavedConfig.module.css';

const [configurations, setConfigurations] = createSignal([
    {config: "SavedConfig #1", _id: 1},
]);

function SavedConfig() {
    return (
        <For each={configurations()}>{(c, _) =>
            <Tile>
                <div class={styles.tileContent}>
                    <div class={styles.description}>{c.config}</div>

                    <div class={styles.openButton}>
                        <button type="button" class="btn btn-info btn-sm" onClick={() =>
                            window.location.replace(`/analyzer/`)
                        }>Open
                        </button>
                    </div>
                </div>
            </Tile>
        }</For>
    );
}

export default SavedConfig;