from typing import List, Tuple
import datetime
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox
from services.algo_service.common.singletons import LAST_RENEW_TIME
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary
from services.algo_service.common.singletons import STRATEGIES


def parse_checkboxes(restriction: Restriction):
    if restriction.upper_border is None:
        restriction.upper_border={index.name: 1 for index in Index}
        restriction.lower_border={index.name: 0 for index in Index}
        if restriction.checkboxes[Checkbox.ONLY_RUSSIAN.name]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_ASSETS.name]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_BONDS.name]:
            pass
        if restriction.checkboxes[Checkbox.WITHOUT_GOLD.name]:
            pass
        if restriction.checkboxes[Checkbox.HIGH_DIVERSIFICATION.name]:
            restriction.upper_border = {k: min(0.1, v) for (k, v) in restriction.upper_border.items()}


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    parse_checkboxes(restriction)
    # While DB isn't fixed.     < datetime.datetime.now():
    if LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime(2009, 10, 10, 0, 0, 0):
        renew_all_data_if_necessary()
    front = list(STRATEGIES.values())  # DEBUG
    best = front[0]
    for ans in front:
        if abs(ans.profit - restriction.target_profit) < abs(best.profit - restriction.target_profit):
            best = ans
    return best, front
