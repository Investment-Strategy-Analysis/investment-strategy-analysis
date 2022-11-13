import {USER_SERVER} from "./web_constants";

export async function loadCheckboxes() {
    const settings = await (await fetch(`${USER_SERVER}/settings/checkboxes`)).json();
    return settings['data'];
}

export async function loadTimePeriods() {
    const settings = await (await fetch(`${USER_SERVER}/settings/analysis_times`)).json();
    return settings['data'];
}

export async function loadStrategies() {
    const settings = await (await fetch(`${USER_SERVER}/settings/strategies`)).json();
    return settings['data'];
}
