const USER_SERVER = "http://localhost:8000";
const ALGO_SERVER = "http://localhost:8001";

const checkboxFormData = [
    { name: "only_russian_assets",  boxid: "onlyRussianAssets" },
    { name: "without_assets",       boxid: "withoutAssets" },
    { name: "without_bonds",        boxid: "withoutBonds" },
    { name: "without_gold",         boxid: "withoutGold" },
    { name: "high_diversification", boxid: "highDiversification" },
];

const timeFormData = [
    { name: "one_year",    radioid: "oneYear",    },
    { name: "three_years", radioid: "threeYears",   },
    { name: "five_years",  radioid: "fiveYears", },
    { name: "ten_years",  radioid: "tenYears", },
];

const initProfit = 50;
const maxProfit = 100;
const minProfit = 0;
const stepProfit = 0.1;

export { USER_SERVER, ALGO_SERVER, checkboxFormData, timeFormData, initProfit, maxProfit, minProfit, stepProfit };
