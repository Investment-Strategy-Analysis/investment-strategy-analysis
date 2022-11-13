from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy
from services.algo_service.common.consts import CHECKBOXES
from services.algo_service.common.singletons import LAST_RENEW_TIME, CURRENT_INDEXES
import datetime
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary
import numpy as np
import operator
import logging
from scipy.optimize import minimize


def parse_checkboxes(restriction: Restriction):
    if restriction.upper_border is None or not restriction.upper_border:
        restriction.upper_border = {i: 1 for i in CURRENT_INDEXES.keys()}
        restriction.lower_border = {i: 0 for i in CURRENT_INDEXES.keys()}
        if restriction.checkboxes[CHECKBOXES[0]]:
            pass
        if restriction.checkboxes[CHECKBOXES[1]]:
            pass
        if restriction.checkboxes[CHECKBOXES[2]]:
            pass
        if restriction.checkboxes[CHECKBOXES[3]]:
            pass
        if restriction.checkboxes[CHECKBOXES[4]]:
            restriction.upper_border = {k: min(0.3, v) for (k, v) in restriction.upper_border.items()}
    logging.info(f'Parsed checkboxes.')


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
    restriction.analysis_time = 1000
    keys = []
    for key in CURRENT_INDEXES.keys():
        if restriction.upper_border[key] > 1e-4:
            keys.append(key)
    data = []
    bounds = []
    for key in keys:
        bounds.append((restriction.lower_border[key],
                       restriction.upper_border[key]))
        data.append(get_history_extended(CURRENT_INDEXES[key].history, restriction.analysis_time))
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
    return (strategy[-1] / strategy[start]) ** (261 / (data.shape[1] - start)), (strategy[1:] - strategy[:-1]).var() * 10000


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
    lowest_profit = 2
    for i in range(len(bounds)):
        distribution = get_x0(bounds, shift=-i)
        tmp_profit, tmp_risk = get_profit_and_risk(data, distribution, invest_period=1)
        rest.append(InvestStrategy(id="Custom", distribution=get_dist(distribution, keys), profit=tmp_profit, risk=tmp_risk))
        if lowest_profit > tmp_profit:
            last_distribution, lowest_profit = distribution, tmp_profit
    for i in np.linspace(restriction.target_profit + 0.95, restriction.target_profit + 1.05, 11):
        best_solutions = []
        _ = minimize(fun=loss_func_creator(best_solutions, data, i, invest_period=1),
                     x0=last_distribution, bounds=bounds, constraints=cons, options={'maxiter': 1000}).x
        rest.append(InvestStrategy(id="Custom", distribution=get_dist(best_solutions[-1][2], keys),
                                   profit=best_solutions[-1][0], risk=best_solutions[-1][1]))
        last_distribution = best_solutions[-1][2]
        print('target = ', i, ' ans = ', best_solutions[-1][0], best_solutions[-1][1])
    best, front = filter_solutions(rest, restriction.target_profit)
    logging.info(f'Algo best = {best}')
    logging.info(f'Algo front = {front}')
    return best, front
