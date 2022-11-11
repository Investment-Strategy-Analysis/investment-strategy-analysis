import {createSignal} from "solid-js";

const USER_SERVER = "http://localhost:8000";
const ALGO_SERVER = "http://localhost:8001";

const [checkboxSettings, setCheckboxSettings] = createSignal([
    {name: "Only russian assets", id: "only_russian_assets"},
    {name: "Without assets", id: "without_assets"},
    {name: "Without bonds", id: "without_bonds"},
    {name: "Without gold", id: "without_gold"},
    {name: "High diversification", id: "high_diversification"},
]);

const [timeSettings, setTimeSettings] = createSignal([
    {name: "1 year", id: "one_year", checked: false},
    {name: "3 years", id: "three_years", checked: false},
    {name: "5 years", id: "five_years", checked: false},
    {name: "10 years", id: "ten_years", checked: true},
]);

const initProfit = 50;
const maxProfit = 100;
const minProfit = 0;
const stepProfit = 0.1;

const [profit, setProfit] = createSignal(initProfit);

const [strategyOption, setStrategyOption] = createSignal([
    {name: "Custom", description: "You can create new strategy!", id: "custom", checkboxes: [], time_period: "ten_years"},
    {name: "Safety", description: "Minimal risk", id: "safety", checkboxes: [], time_period: "five_year"},
    {name: "Risky", description: "Maximal profit", id: "risky", checkboxes: [], time_period: "one_year"},
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
