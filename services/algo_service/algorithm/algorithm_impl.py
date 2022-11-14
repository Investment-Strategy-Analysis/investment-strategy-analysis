import datetime
import logging
from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox
from services.algo_service.common.singletons import STRATEGIES, LAST_RENEW_TIME, CURRENT_INDEXES
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary
import numpy as np
import operator
import logging
from scipy.optimize import minimize


def parse_checkboxes(restriction: Restriction):
    if restriction.upper_border is None or restriction.upper_border == {}:
        restriction.upper_border = {index.value.id: 1 for index in Index}
        restriction.lower_border = {index.value.id: 0 for index in Index}
        if restriction.checkboxes[Checkbox.ONLY_RUSSIAN.value.id]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_ASSETS.value.id]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_BONDS.value.id]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_GOLD.value.id]:
            pass
        if restriction.checkboxes[Checkbox.HIGH_DIVERSIFICATION.value.id]:
            restriction.upper_border = {k: min(0.1, v) for (k, v) in restriction.upper_border.items()}
    logging.info(f'Parsed checkboxes. Restriction = {restriction}')


def get_data_matrix(data: list):
    max_len = max(map(len, data))
    return np.array([
        [None] * (max_len - len(x)) + [1] + list(map(operator.truediv, x[1:], x[:-1]))
        for x in data], dtype=np.float)


def get_history_extended(history, analysis_time):
    if analysis_time <= len(history):
        return history[-analysis_time:]
    else:
        return [history[0]] * (analysis_time - len(history)) + history


def get_right_input(restriction):
    keys = []

    for key in CURRENT_INDEXES.keys():
        if restriction.upper_border[key] > 1e-4:
            keys.append(key)
    data = []
    bounds = []
    for key in keys:
        bounds.append((restriction.lower_border[key],
                       restriction.upper_border[key]))
        data.append(get_history_extended(CURRENT_INDEXES[key].history, int(restriction.analysis_time) * 5 // 7))
    return get_data_matrix(data), bounds, keys


def get_profit_and_risk(data, distribution, invest_period=1):
    strategy = np.zeros((data.shape[1],))
    current_distribution = np.zeros((data.shape[0],))
    start = data.shape[1]
    for i in range(distribution.shape[0]):
        if distribution[i] > 0.001:
            start = min(start, np.nonzero(np.logical_not(np.isnan(data[i, :])))[0][0])
    strategy[start] = 1
    for i in range(start + 1, data.shape[1]):
        data_none = np.logical_not(np.isnan(data[:, i]))
        if i % invest_period == 0:
            current_distribution[data_none] = distribution[data_none]
            current_distribution /= np.sum(current_distribution) / strategy[i - 1]
        current_distribution[data_none] = current_distribution[data_none] * data[data_none, i]
        strategy[i] = current_distribution.sum()
    return (strategy[-1] / strategy[start]) ** (261 / (data.shape[1] - start)) * 100, (strategy[1:] - strategy[:-1]).var()


def loss_func_creator(all_solutions, data: np, target_profit=1.1, invest_period=1):
    def loss_func(distribution):
        profit, risk = get_profit_and_risk(data, np.array(distribution), invest_period)
        all_solutions.append([profit, risk, distribution])
        loss = (profit - target_profit)**4 + abs(profit - target_profit)**0.5 + risk  # TODO not ideal
        return loss
    return loss_func


def get_x0(bounds, shift=0):
    answer = [0] * len(bounds)
    for i in range(len(bounds)):
        answer[i] = bounds[i][0]
    for i in range(len(bounds)):
        needs = 1 - sum(answer)
        if needs > bounds[i + shift][1] - bounds[i + shift][0]:
            answer[i + shift] = bounds[i + shift][1]
        else:
            answer[i + shift] += 1 - sum(answer)
    return np.array(answer)


def get_dist(distribution, keys):
    return {keys[i]: distribution[i] for i in range(len(keys))}


def filter_solutions(rest, target_profit):
    front = []
    for i in rest:
        is_unique = True
        for j in front:
            if abs(j.profit - i.profit) < 0.001:
                if i.profit < j.profit:
                    j = i
                is_unique = False
                break
        if is_unique:
            front.append(i)
    best = front[0]
    for i in front:
        if i.profit - target_profit > 0.999 >= best.profit - target_profit:
            best = i
        if i.profit - target_profit > 0.999 and i.risk < best.risk:
            best = i
    return best, front


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    global LAST_RENEW_TIME
    parse_checkboxes(restriction)
    if LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime.now():
        renew_all_data_if_necessary()
        LAST_RENEW_TIME = datetime.datetime.now()
    data, bounds, keys = get_right_input(restriction)
    cons = ({'type': 'eq', 'fun': lambda x: 1 - sum(x)})
    rest = []
    last_distribution = get_x0(bounds)
    risk_normalization = get_profit_and_risk(data, last_distribution, invest_period=1)[1] * 0.01
    logging.info(f'Risk Normalization = {risk_normalization}')
    for i in np.linspace(restriction.target_profit + 95, restriction.target_profit + 105, 11):
        best_solutions = []
        _ = minimize(fun=loss_func_creator(best_solutions, data, i, invest_period=1),
                     x0=last_distribution, bounds=bounds, constraints=cons, options={'maxiter': 1000}).x
        rest.append(InvestStrategy(id="Custom", distribution=get_dist(best_solutions[-1][2], keys),
                                   profit=best_solutions[-1][0], risk=best_solutions[-1][1] / risk_normalization))
        last_distribution = best_solutions[-1][2]
        print('target = ', i, ' ans = ', best_solutions[-1][0], best_solutions[-1][1] / risk_normalization)
    best, front = filter_solutions(rest, restriction.target_profit)
    logging.info(f'Algo best = {best}')
    logging.info(f'Algo front = {front}')
    return best, front
