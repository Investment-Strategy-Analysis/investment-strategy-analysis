import styles from './SettingsTile.module.css';
import {createEffect, createSignal, For} from 'solid-js';

import Tile from "../Tile/Tile";
import SettingCheckbox from "../SettingCheckbox/SettingCheckbox";
import SettingRadio from "../SettingRadio/SettingRadio";
import {checkboxSettings, timeSettings} from "../../js/web_constants";

function SettingsTile() {
    const activateVerticalMode = (width) => 768 < width && width <= 992
    const [timeButtonClass, setTimeButtonClass] = createSignal("btn-group")
    window.onresize = (event) => {
        setTimeButtonClass(activateVerticalMode(window.innerWidth) ? "btn-group-vertical" : "btn-group")
    }

    return (
        <Tile>
            <div class="block">
                <form id="settingsForm" method="post">
                    <h5>Settings</h5>
                    <For each={checkboxSettings()}>{(checkbox, _) =>
                        <SettingCheckbox name={checkbox.name} boxid={checkbox.id}/>
                    }</For>

                    <hr/>
                    <h5>Time period</h5>
                    <div class={timeButtonClass()} id={styles.ButtonGroup} role="group" aria-label="Time period">
                        <For each={timeSettings()}>{(radio, _) =>
                            <SettingRadio name={radio.name} radioid={radio.id} groupname="timeRadio" checked={radio.checked}/>
                        }</For>
                    </div>
                </form>
            </div>
        </Tile>
    );
}

export default SettingsTile;
