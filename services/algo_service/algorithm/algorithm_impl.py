from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy
from services.algo_service.common.consts import CHECKBOXES
from services.algo_service.common.singletons import LAST_RENEW_TIME, CURRENT_INDEXES
import logging
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary


def parse_checkboxes(restriction: Restriction):
    if restriction.upper_border is None:
        restriction.upper_border={i: 1 for i in CURRENT_INDEXES.keys()}
        restriction.lower_border={i: 0 for i in CURRENT_INDEXES.keys()}
        if restriction.checkboxes[CHECKBOXES[0]]:
            pass
        if restriction.checkboxes[CHECKBOXES[1]]:
            pass
        if restriction.checkboxes[CHECKBOXES[2]]:
            pass
        if restriction.checkboxes[CHECKBOXES[3]]:
            pass
        if restriction.checkboxes[CHECKBOXES[4]]:
            restriction.upper_border = {k: min(0.1, v) for (k, v) in restriction.upper_border.items()}


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    parse_checkboxes(restriction)
    # While DB isn't fixed.     < datetime.datetime.now():
    # if LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime(2009, 10, 10, 0, 0, 0):
    #    renew_all_data_if_necessary()
    front = [  # DEBUG
        InvestStrategy(profit=1.25, risk=10, distribution={'RTSI': 1,'RTSOG': 0}),
        InvestStrategy(profit=1.20, risk=7, distribution={'RTSI': 0.75,'RTSOG': 0.25}),
        InvestStrategy(profit=1.15, risk=5, distribution={'RTSI': 0.5,'RTSOG': 0.5}),
        InvestStrategy(profit=1.10, risk=4, distribution={'RTSI': 0.25,'RTSOG': 0.75}),
        InvestStrategy(profit=1.05, risk=5, distribution={'RTSI': 0,'RTSOG': 1})
    ]
    best = front[0]
    for ans in front:
        if abs(ans.profit - 1 - restriction.target_profit) < abs(best.profit - 1 - restriction.target_profit):
            best = ans
    logging.info(f"Target = {restriction.target_profit}, Best = {best}, Front = {front}")
    return best, front
