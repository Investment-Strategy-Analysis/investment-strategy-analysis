import { chartData } from '../GraphicTile/GraphicTile';
import SolidChart from "solid-charts-js";

function Charts() {

  return (
    <>
      {chartData() &&
        <SolidChart
          {...chartData()}
          canvasOptions={{
            width: 200,
            height: 150
          }}
        />
      }

    </>
  );
}

export default Charts;
