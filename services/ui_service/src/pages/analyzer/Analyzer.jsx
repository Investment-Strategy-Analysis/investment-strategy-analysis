import styles from './Analyzer.css';
import RiskTile from "../../components/RiskTile/RiskTile";
import StrategyTile from "../../components/StrategyTile/StrategyTile";
import SettingsTile from "../../components/SettingsTile/SettingsTile";
import GraphicTile, {setChartData, transformData} from "../../components/GraphicTile/GraphicTile";
import {ALGO_SERVER, checkboxFormData, timeFormData} from "../../js/web_constants";

function constructRequestBody() {
    let body = {};

    let params = {};
    checkboxFormData.forEach(element => params[element.name] = document.getElementById(element.boxid).checked);
    timeFormData.forEach(element => params[element.name] = document.getElementById(element.radioid).checked);

    body["target_profit"] = document.getElementById("profitRange").value / 100
    body["checkboxes"] = params;
    body["upper_border"] = {}
    body["lower_border"] = {}
    body["analysis_time"] = 0

    return body;
}

function Analyzer() {

    async function getSolution(body) {
        const options = {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json;charset=utf-8"
            }
        }
        const response = await fetch(
            `${ALGO_SERVER}/solutions`,
            options,
        );

        if (response.ok) {
            const data = await response.json();
            const chartDataset = data[1].sort((a, b) => a.profit - b.profit);
            setChartData(transformData(chartDataset));
        }
    }

    return (
        <>
            <div class="container-md">
                <div class="row mb-2">
                    <div class="col-md-4">
                        <RiskTile/>
                    </div>
                    <div class="col-md-8">
                        <StrategyTile/>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-4">
                        <SettingsTile/>
                        <button type="button" class="btn btn-primary btn-lg run-button" onClick={() => getSolution(constructRequestBody())}>Find optimal configuration</button>
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