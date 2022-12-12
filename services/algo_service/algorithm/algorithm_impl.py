import datetime
from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox
import services.algo_service.common.singletons as singletons
from services.algo_service.common.consts import RESORT_COUNT
from services.algo_service.db.data_pull_foreign import renew_foreign_data_if_necessary
from services.algo_service.db.data_pull_russia import renew_russian_data_if_necessary
import numpy as np
import operator
import logging
import cvxpy as cp


def parse_checkboxes(restriction: Restriction):
    # Принимает на вход ограничения выставленные пользователем.
    # Проверяет если в ограничениях нет выставленных в ручную параметров (то есть нет upper_border и lower_border)
    # тогда он их заполняет с учётом галочек. В данный момент нет всех активов, чтоб написать эту функцию корректно.
    if restriction.upper_border is None or restriction.upper_border == {}:
        restriction.upper_border = {index.value.id: 1 for index in Index}
        restriction.lower_border = {index.value.id: 0 for index in Index}
        to_zero = []
        if restriction.checkboxes[Checkbox.ONLY_RUSSIAN.value.id]:
            to_zero += ["SPX", "GDAXI", "IXIC", "USD"]
        if restriction.checkboxes[Checkbox.WITHOUT_ASSETS.value.id]:
            to_zero += ["SPX", "GDAXI", "IXIC", "IMOEX"]
        if restriction.checkboxes[Checkbox.WITHOUT_BONDS.value.id]:
            to_zero += ["MCXSM"]
        if restriction.checkboxes[Checkbox.WITHOUT_GOLD.value.id]:
            to_zero += ["GOLD"]
        if restriction.checkboxes[Checkbox.HIGH_DIVERSIFICATION.value.id]:
            restriction.upper_border = {k: min(0.3, v) for (k, v) in restriction.upper_border.items()}
        for i in to_zero:
            restriction.upper_border[i] = 0
    logging.info(f'Parsed checkboxes. Restriction = {restriction}')


def get_data_matrix(data: list):
    # Принимает на вход список списков, который превращает в np.array с 1 до первой информации о активе
    # Так же схлопывает все дни в блоки между обновлениями.
    if len(data) == 0:
        return np.array([], dtype=np.float)
    
    max_len = max(map(len, data))
    shape_of_reshape = max_len // RESORT_COUNT
    for i in range(len(data)):
        data[i] = np.reshape(
            [1] * (max_len - len(data[i]) + 1) + list(map(operator.truediv, data[i][1:], data[i][:-1])),
            (-1, shape_of_reshape)
        ).prod(axis=-1)
    return np.array(data, dtype=np.float)


def get_history_extended(history, analysis_time: int):
    # Принимает список истории и время, которое мы хотим отрезать. Добавляет пару дней для делимости на RESORT_COUNT.
    # Если список короче времени, возвращаем что есть.
    analysis_time = (analysis_time + RESORT_COUNT - 1) // RESORT_COUNT * RESORT_COUNT
    if analysis_time <= len(history):
        return history[-analysis_time:]
    else:
        return history


def get_right_input(restriction):
    # Принимает ограничения и возвращает их в другой форме.
    # Убирает все активы, которые не входят в ответ изначально.
    # Возвращает numpy матрицу усечённую по неиспользуемым активам и RESORT_COUNT длинной
    # два numpy массива ограничений снизу, сверху и лист названий соответствующих активов.
    keys = []
    for key in singletons.CURRENT_INDEXES.keys():
        if restriction.upper_border.get(key, 0) > 1e-4:
            keys.append(key)
    data = []
    lower = np.zeros((len(keys),))
    upper = np.ones((len(keys),))
    for i in range(len(keys)):
        lower[i] = restriction.lower_border[keys[i]]
        upper[i] = restriction.upper_border[keys[i]]
        data.append(
            get_history_extended(
                singletons.CURRENT_INDEXES[keys[i]].history,
                int(restriction.analysis_time) * 5 // 7
            )
        )
    return get_data_matrix(data), lower, upper, keys


def find_max(D, lower, upper, years_count):
    # Ищет максимально возможный доход, не обращая внимания на риск.
    d = cp.Variable((D.shape[0],))
    D = D.T
    prob = cp.Problem(
        cp.Maximize(cp.geo_mean(D @ d)),
        [d >= lower, d <= upper, cp.norm(d, 1) <= 1.0]
    )
    prob.solve()
    return d.value, np.prod(D @ d.value)**(1 / years_count), np.var(D @ d.value)


def find_best(D, lower, upper, target_profit, x0, years_count):
    # Ищет наименьший риск при доходе больше таргета.
    target_profit **= years_count / D.shape[1]
    d = cp.Variable((D.shape[0],))
    if x0 is not None:
        d.value = x0
    D = D.T
    prob = cp.Problem(
        cp.Minimize(
            cp.sum(cp.power(D @ d - cp.sum(D @ d) / D.shape[1], 2)) / D.shape[1]
        ),
        [d >= lower, d <= upper, cp.norm(d, 1) <= 1.0, target_profit <= cp.geo_mean(D @ d)]
    )
    prob.solve()
    return d.value, np.prod(D @ d.value)**(1 / years_count), np.var(D @ d.value)


def get_dict(distribution, keys):
    # Принимает лист распределения и лист названий, возвращает словарь из них.
    return {keys[i]: distribution[i] for i in range(len(keys))}


def filter_solutions(rest, target_profit):
    # Принимает лист решений и целевую доходность.
    # Возвращает наилучшее решение, чья доходность >= целевой и имеет наименьший риск.
    # Возвращает лист оптимальных и не повторяющихся значений. (бывают как идентичные, так и очень близкие).
    # А так же убирает не эффективные решения, если есть более выгодные.
    front = []
    for i in rest:
        is_unique = True
        for j in range(len(front)):
            if abs(front[j].profit - i.profit) < 0.001:
                if i.profit < front[j].profit:
                    front[j] = i
                is_unique = False
                break
        if is_unique:
            front.append(i)
    best = front[-1]
    for i in front:
        if abs(i.profit - target_profit) < abs(best.profit - target_profit):
            best = i
    return best, front


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    # Принимает на вход ограничения. Преобразует их, если необходимо.
    # Если прошёл хотя бы час с прошлого обновления делает новый запрос по данным.
    # Находит оптимальный ответ и все ответы находящиеся на парето фронте.
    parse_checkboxes(restriction)
    if singletons.LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime.now():
        renew_russian_data_if_necessary()
        renew_foreign_data_if_necessary()
        singletons.LAST_RENEW_TIME = datetime.datetime.now()
    years_count = int(restriction.analysis_time) / 365
    data, lower, upper, keys = get_right_input(restriction)
    dist, profit, risk = find_max(data, lower, upper, years_count)
    last_distribution = dist
    risk_norm = max(1e-7, float(risk))
    print('target = max', ' ans = ', profit, ' risk_norm = ', risk_norm, ' risk = ', risk)
    solutions = [InvestStrategy(id="Custom", distribution=get_dict(dist, keys), profit=profit * 100, risk=100)]
    for i in np.flip(np.linspace(1, max(1.0, int(profit * 100) / 100), 1 + int((profit - 1) * 100))):
        dist, profit, risk = find_best(data, lower, upper, i, last_distribution, years_count)
        solutions.append(InvestStrategy(id="Custom", distribution=get_dict(dist, keys),
                                        profit=profit * 100, risk=risk / risk_norm * 100))
        last_distribution = dist
        print('target = ', i, ' ans = ', profit, risk / risk_norm)
    best, front = filter_solutions(solutions, restriction.target_profit + 100)
    logging.info(f'Algo best = {best}')
    logging.info(f'Algo front = {front}')
    return best, front