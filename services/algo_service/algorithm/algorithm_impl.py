from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy
from services.algo_service.common.singletons import LAST_RENEW_TIME
import datetime
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    if LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime.now():
        renew_all_data_if_necessary()

    front = [  # DEBUG
        InvestStrategy(profit=25, risk=10, distribution={'RTSI': 1,'MOEXBC': 0}),
        InvestStrategy(profit=20, risk=7, distribution={'RTSI': 0.75,'MOEXBC': 0.25}),
        InvestStrategy(profit=15, risk=5, distribution={'RTSI': 0.5,'MOEXBC': 0.5}),
        InvestStrategy(profit=10, risk=4, distribution={'RTSI': 0.25,'MOEXBC': 0.75}),
        InvestStrategy(profit=5, risk=5, distribution={'RTSI': 0,'MOEXBC': 1})
    ]
    best = front[0]
    for ans in front:
        if abs(ans.profit - restriction.target_profit) < abs(best.profit - restriction.target_profit):
            best = ans
    return best, front
