import styles from './App.css';
import NavBar from "./components/NavBar/NavBar";
import RiskTile from "./components/RiskTile/RiskTile";
import StrategyTile from "./components/StrategyTile/StrategyTile";
import SettingsTile from "./components/SettingsTile/SettingsTile";
import GraphicTile from "./components/GraphicTile/GraphicTile";

function App() {
    return (
        <>
            <NavBar/>
            <div class="container">
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
                        <button type="button" class="btn btn-primary btn-lg run-button">Find optimal configuration</button>
                    </div>
                    <div class="col-md-8">
                        <GraphicTile/>
                    </div>
                </div>
            </div>
        </>
    );
}

export default App;
