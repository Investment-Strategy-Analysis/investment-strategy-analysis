import styles from './Analyzer.css';
import NavBar from "../NavBar/NavBar";
import RiskTile from "../RiskTile/RiskTile";
import StrategyTile from "../StrategyTile/StrategyTile";
import SettingsTile from "../SettingsTile/SettingsTile";
import GraphicTile from "../GraphicTile/GraphicTile";

function Analyzer() {
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

export default Analyzer;
