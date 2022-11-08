import {createSignal} from "solid-js";

const USER_SERVER = "http://localhost:8000";
const ALGO_SERVER = "http://localhost:8001";

const [checkboxSettings, setCheckboxSettings] = createSignal([
    {name: "Only russian assets", boxid: "onlyRussianAssets"},
    {name: "Without assets", boxid: "withoutAssets"},
    {name: "Without bonds", boxid: "withoutBonds"},
    {name: "Without gold", boxid: "withoutGold"},
    {name: "High diversification", boxid: "highDiversification"},
]);

const [timeSettings, setTimeSettings] = createSignal([
    {name: "1 year", radioid: "oneYear", checked: false},
    {name: "3 years", radioid: "threeYears", checked: false},
    {name: "5 years", radioid: "fiveYears", checked: false},
    {name: "10 years", radioid: "tenYears", checked: true},
]);

const initProfit = 50;
const maxProfit = 100;
const minProfit = 0;
const stepProfit = 0.1;

const [profit, setProfit] = createSignal(initProfit);

const [strategyOption, setStrategyOption] = createSignal([
    {name: "Custom", description: "You can create new strategy!", id: "custom"},
    {name: "Safety", description: "Minimal risk", id: "safety"},
    {name: "Risky", description: "Maximal profit", id: "risky"},
]);

const [strategy, setStrategy] = createSignal(strategyOption()[0])

export {
    USER_SERVER,
    ALGO_SERVER,
    checkboxSettings,
    setCheckboxSettings,
    timeSettings,
    setTimeSettings,
    initProfit,
    maxProfit,
    minProfit,
    stepProfit,
    profit,
    setProfit,
    strategyOption,
    setStrategyOption,
    strategy,
    setStrategy
};
