import { createSignal, For } from 'solid-js';

import Tile from "../Tile/Tile";
import SettingCheckbox from "../SettingCheckbox/SettingCheckbox";
import SettingRadio from "../SettingRadio/SettingRadio";

function SettingsTile() {
    const [ checkboxSettings, setCheckboxSettings ] = createSignal([
        { name: "Only russian assets",  boxid: "onlyRussianAssets" },
        { name: "Without assets",       boxid: "withoutAssets" },
        { name: "Without bonds",        boxid: "withoutBonds" },
        { name: "Without gold",         boxid: "withoutGold" },
        { name: "High diversification", boxid: "highDiversification" },
    ]);

    const [ timeSettings, setTimeSettings ] = createSignal([
        { name: "1 year",  radioid: "oneYear",    groupname: "timeRadio", checked: true },
        { name: "3 years", radioid: "twoYears",   groupname: "timeRadio", checked: false },
        { name: "5 years", radioid: "threeYears", groupname: "timeRadio", checked: false },
    ]);

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
                            <SettingRadio name={radio.name} radioid={radio.radioid} groupname={radio.groupname} checked={radio.checked}/>
                        }</For>
                    </div>
                </form>
            </div>
        </Tile>
    );
}

export default SettingsTile;
