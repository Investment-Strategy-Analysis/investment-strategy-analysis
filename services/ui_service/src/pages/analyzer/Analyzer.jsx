import styles from './Analyzer.css';
import ProfitTile from "../../components/ProfitTile/ProfitTile";
import StrategyTile from "../../components/StrategyTile/StrategyTile";
import SettingsTile from "../../components/SettingsTile/SettingsTile";
import GraphicTile, {setChartData, transformData} from "../../components/GraphicTile/GraphicTile";
import {USER_SERVER} from "../../js/web_constants";
import {
    resultProfit, resultProfitPoints,
    ResultTile,
    setResultProfit,
    setResultProfitPoints,
    setResults
} from "../../components/ResultTile/ResultTile";
import {
    checkboxSettings,
    setCheckboxSettings,
    timeSettings,
    profit,
    setStrategyOption, setSolutionLoaded, strategy, setProfit
} from "../../js/settings";
import {loadCheckboxes, loadStrategies, loadTimePeriods} from "../../js/settings_loader";
import {createSignal, Show} from "solid-js";
import {timeToInt} from "../../js/utils";

/**
 * Generate settings request body
 * @return {object}
 */
function constructRequestBody() {
    let body = {};
    let params = {};

    let time_period = timeSettings().filter(element => document.getElementById(element.id).checked)[0].days;
    checkboxSettings().forEach(element => params[element.id.toUpperCase()] = document.getElementById(element.id).checked);

    body["target_profit"] = +(profit())
    body["checkboxes"] = params;
    body["analysis_time"] = time_period;
    body["upper_border"] = {}
    body["lower_border"] = {}

    return body;
}

async function saveRestrictions(settings, risk) {
    let body = {
        strategy: strategy().id,
        restrictions: settings,
        risk: risk
    }

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

async function loadRestrictions() {
    const access_token = Cookies.get('ACCESS_TOKEN');
    const options = {
        method: "GET",
        headers: {
            'accept': 'application/json',
            'Authorization': `Bearer ${access_token}`,
            "Content-Type": "application/json;charset=utf-8"
        }
    }
    const response = await fetch(
        `${USER_SERVER}/user/current_settings`,
        options,
    );
    if (response.ok) {
        const data = await response.json();
        setProfit(data.restrictions.target_profit);
        const checkboxes = data.restrictions.checkboxes;
        const time = data.restrictions.analysis_time;
        checkboxSettings().forEach(checkbox => document.getElementById(checkbox.id).checked = checkboxes[checkbox.id])
        timeSettings().forEach(timeButton => document.getElementById(timeButton.id).checked = timeToInt(timeButton.id) == time);
    }
}

/**
 * Make solution request
 * @return {Promise<void>}
 */
async function getSolution() {
    let body = constructRequestBody()

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
    setSolutionLoaded(false);
    const response = await fetch(
        `${USER_SERVER}/solutions`,
        options,
    );

    if (response.ok) {
        const data = await response.json();
        const chartDataset = data[1].sort((a, b) => a.profit - b.profit);
        const bestDistribution = data[0]['distribution'];
        const config = Object.keys(bestDistribution).map((key) => [key, bestDistribution[key]]);
        const bestProfit = data[0]['profit'];
        const bestPoint = data[1].map((point) => point.profit === bestProfit ? point.risk : null )

        setSolutionLoaded(true);
        setResults(() => config);
        setResultProfit(() => {
            return {
                profit: bestProfit,
                distribution : bestDistribution
            }
        });
        setResultProfitPoints(() => {
            return chartDataset.map(it => {
                return {
                    profit: it.profit,
                    distribution: it.distribution
                }
            })
        })
        setChartData(transformData(chartDataset, bestPoint));
        await saveRestrictions(body, data[0]['risk']);
    } else {
        window.location.replace("/auth/login/");
    }
}

function Analyzer() {
    loadCheckboxes().then(it => setCheckboxSettings(it));
    // loadTimePeriods().then(it => {
    //     const times = it.slice(2, it.length);
    //     times.forEach(time => time.checked = false);
    //     times[0].checked = true;
    //     setTimeSettings(times);
    // });
    loadRestrictions().then(r => console.log("Restriction was loaded"));

    // loadStrategies().then(it => setStrategyOption(it));

    return (
        <>
            <div class="container-lg">
                <div class="row mb-2">
                    <div class="col-md-4">
                        <ProfitTile/>
                    </div>
                    <div class="col-md-8">
                        <StrategyTile/>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-4">
                        <SettingsTile/>
                        <button type="button" class="btn btn-primary btn-lg run-button" onClick={() => getSolution()}>Find optimal configuration</button>
                        <ResultTile/>
                    </div>
                    <div class="col-md-8">
                        <GraphicTile/>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Analyzer;