import Tile from "../Tile/Tile";
import {createSignal, createEffect} from "solid-js";
import styles from './GraphicTile.module.css';
import Charts from '../Chart/Chart';
import {formatFloat} from "../../js/utils";

const [chartData, setChartData] = createSignal({});

function transformData(dataset, bestPoint) {
    let mainColor = "#3BE9E9";
    let bestColor = "#80ea29";
    let bestBackgroundColor = "#b7e88f";

    return {
        type: "line",
        data: {
            labels: dataset.map((d) => formatFloat(d.profit)),
            datasets: [
                {
                    label: "The best configuration",
                    fill: false,
                    data: bestPoint.map(formatFloat),
                    borderColor: bestColor,
                    pointBackgroundColor: bestBackgroundColor,
                    pointBorderWidth: 0,
                    pointRadius: 9,
                    pointHoverRadius: 10,
                },
                {
                    label: "risk(profit)",
                    fill: false,
                    data: dataset.map((d) => formatFloat(d.risk)),
                    borderColor: mainColor,
                    pointBackgroundColor: mainColor,
                    pointBorderWidth: 3,
                    pointRadius: 4,
                    pointHoverRadius: 9,
                },
            ],
        },
        options: {
            scales: {
                xAxes: [{
                    offset: true,
                    gridLines: {
                        offsetGridLines: false,
                        display: true,
                        borderDash: [6, 2],
                        tickMarkLength: 5
                    },
                }],
                yAxes: [{
                    offset: true,
                    gridLines: {
                        offsetGridLines: false,
                        display: true,
                        borderDash: [6, 2],
                        tickMarkLength: 5
                    },
                }]
            },
        }
    }
}


function GraphicTile() {

    createEffect(() => {
        // setChartData(transformData([]))
    });

    return (
        <Tile>
            <div class={styles.GraphicTile}>
                <h3><b>Risk</b> vs <b>Profit</b></h3>
                <Charts/>
            </div>
        </Tile>
    );
}

export {chartData, setChartData, transformData}

export default GraphicTile;