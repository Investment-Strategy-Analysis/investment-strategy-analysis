from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy
from services.algo_service.common.singletons import LAST_RENEW_TIME
import datetime
from services.algo_service.db.data_pull_russia import renew_all_data_if_necessary
from services.algo_service.common.singletons import CURRENT_INDEXES


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    # While DB isn't fixed.     < datetime.datetime.now():
    if LAST_RENEW_TIME + datetime.timedelta(hours=1) < datetime.datetime(2009, 10, 10, 0, 0, 0):
        print(CURRENT_INDEXES)
        renew_all_data_if_necessary()
        print(CURRENT_INDEXES)

    front = [  # DEBUG
        InvestStrategy(profit=25, risk=10, distribution={'RTSI': 1,'RTSOG': 0}),
        InvestStrategy(profit=20, risk=7, distribution={'RTSI': 0.75,'RTSOG': 0.25}),
        InvestStrategy(profit=15, risk=5, distribution={'RTSI': 0.5,'RTSOG': 0.5}),
        InvestStrategy(profit=10, risk=4, distribution={'RTSI': 0.25,'RTSOG': 0.75}),
        InvestStrategy(profit=5, risk=5, distribution={'RTSI': 0,'RTSOG': 1})
    ]
    best = front[0]
    for ans in front:
        if abs(ans.profit - restriction.target_profit) < abs(best.profit - restriction.target_profit):
            best = ans
    return best, front
