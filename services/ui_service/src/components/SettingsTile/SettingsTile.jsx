import { createSignal, For } from 'solid-js';

import Tile from "../Tile/Tile";
import SettingCheckbox from "../SettingCheckbox/SettingCheckbox";
import SettingRadio from "../SettingRadio/SettingRadio";
import {checkboxSettings, timeSettings} from "../../js/web_constants";

function SettingsTile() {

    return (
        <Tile>
            <div class="block">
                <form id="settingsForm" method="post">
                    <h5>Settings</h5>
                    <For each={checkboxSettings()}>{(checkbox, _) =>
                        <SettingCheckbox name={checkbox.name} boxid={checkbox.boxid}/>
                    }</For>

                    <hr/>
                    <h5>Time period</h5>
                    <div class="btn-group" role="group" aria-label="Time period">
                        <For each={timeSettings()}>{(radio, _) =>
                            <SettingRadio name={radio.name} radioid={radio.radioid} groupname="timeRadio" checked={radio.checked}/>
                        }</For>
                    </div>
                </form>
            </div>
        </Tile>
    );
}

export default SettingsTile;
