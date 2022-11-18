import {createSignal} from "solid-js";

const [checkboxSettings, setCheckboxSettings] = createSignal([]);

const [timeSettings, setTimeSettings] = createSignal([]);

const [strategyOption, setStrategyOption] = createSignal([
    {name: "Custom", description: "You can create new strategy!", id: "custom", checkboxes: [], time_period: "YEAR_1"},
    {name: "Safety", description: "Minimal risk", id: "safety", checkboxes: ["ONLY_RUSSIAN"], time_period: "YEAR_5"},
    {name: "Risky", description: "Maximal profit", id: "risky", checkboxes: ["HIGH_DIVERSIFICATION"], time_period: "YEAR_3"},
]);

const [strategy, setStrategy] = createSignal(strategyOption()[0])

const [solutionLoaded, setSolutionLoaded] = createSignal(null);

const initProfit = 14.5;
const maxProfit = 100;
const minProfit = 0;
const stepProfit = 0.1;

const [profit, setProfit] = createSignal(initProfit);

export {
    checkboxSettings,
    setCheckboxSettings,
    timeSettings,
    setTimeSettings,
    strategyOption,
    setStrategyOption,
    strategy,
    setStrategy,
    initProfit,
    maxProfit,
    minProfit,
    stepProfit,
    profit,
    setProfit,
    solutionLoaded,
    setSolutionLoaded,
};
