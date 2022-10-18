import Tile from "../Tile/Tile";
import {createSignal, createEffect} from "solid-js";
import styles from './GraphicTile.module.css';
import Charts from '../Chart/Chart';

const [chartData, setChartData] = createSignal({});

function transformData(dataset) {
    return {
        type: "line",
        data: {
            labels: dataset.map((d) => d.profit),
            datasets: [
                {
                    label: "risk(profit)",
                    fill: false,
                    data: dataset.map((d) => (d.risk)),
                    borderColor: "#3BE9E9"
                }
            ]
        },
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