import styles from './Analyzer.css';
import ProfitTile from "../../components/ProfitTile/ProfitTile";
import StrategyTile from "../../components/StrategyTile/StrategyTile";
import SettingsTile from "../../components/SettingsTile/SettingsTile";
import GraphicTile, {setChartData, transformData} from "../../components/GraphicTile/GraphicTile";
import {ALGO_SERVER, checkboxFormData, timeFormData} from "../../js/web_constants";
import {ResultTile, setResults} from "../../components/ResultTile/ResultTile";

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
            const bestDistribution = data[0]['distribution'];
            const config = Object.keys(bestDistribution).map((key) => [key, bestDistribution[key]]);
            const bestProfit = data[0]['profit'];
            const bestPoint = data[1].map((point) => point.profit === bestProfit ? point.risk : null )

            setResults(config);
            setChartData(transformData(chartDataset, bestPoint));
        }
    }

    return (
        <>
            <div class="container-md">
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
                        <button type="button" class="btn btn-primary btn-lg run-button" onClick={() => getSolution(constructRequestBody())}>Find optimal configuration</button>
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