import Tile from "../Tile/Tile";
import { createSignal, createEffect } from "solid-js";
import styles from './GraphicTile.module.css';
import Charts from '../Chart/Chart';

const [chartData, setChartData] = createSignal({});

createEffect(() => {
  const fetchData = async () => {
    const res = await fetch("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=2c36818bb5ca9e829313dd736fd15859")
    const data = await res.json();

    setChartData({
      type: "line",
      data: {
        labels: data.map((d) => ""),
        datasets: [
          {
            label: "???",
            fill: false,
            // backgroundColor: [
            //   "#0d6efd",
            //   "#28a745",
            //   "#dc3545",
            //   "#ffc107",
            //   "#17a2b8",
            //
            // ],
            data: data.map((d) => (d.lat))
          }
        ]
      }
    })

  }
  fetchData()
});


function GraphicTile() {

  return (
      <Tile>
          <div class={styles.GraphicTile}>
              <h3><b>Risk</b> vs <b>Profit</b></h3>
              <Charts />
          </div>
      </Tile>
  );
}

export { chartData }

export default GraphicTile;