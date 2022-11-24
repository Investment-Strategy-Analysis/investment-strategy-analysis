from datetime import datetime

import pytest

from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox
from services.algo_service.algorithm.algorithm_impl import get_solutions as __get_solutions
import services.algo_service.common.singletons as singles


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    return __get_solutions(restriction)


best_invest_strat = InvestStrategy(id='Custom',
                                   description=None,
                                   profit=112.99998084763949,
                                   risk=44.24218097256038,
                                   distribution={'IMOEX': 0.2731227341646331,
                                                 'MOEXBC': 0.05215926660875515,
                                                 'MOEXBMI': 0.28516439616922346,
                                                 'MCXSM': 0.38955360305738834})


def compare_invest_starts(strat1: InvestStrategy, strat2: InvestStrategy):
    return strat1.risk == strat2.risk and strat1.profit == strat2.profit


test_data_restriction = [
    Restriction(target_profit=13,
                checkboxes={checkbox.value.id: False for checkbox in Checkbox},
                upper_border={index.value.id: 1 for index in Index},
                lower_border={index.value.id: 0 for index in Index},
                analysis_time=100),

]


@pytest.mark.parametrize("restrict", test_data_restriction)
def test_example(restrict: Restriction):
    # global LAST_RENEW_TIME
    # for val in singles.CURRENT_INDEXES.vals():
    #     val.history = [1, 3, 4, 6]
    # singles.LAST_RENEW_TIME = datetime.datetime.now()
    print(restrict)
    best, front = get_solutions(restrict)
    print(best)
    print(best_invest_strat)
    assert best.risk == 44.24218097256038
    assert best.profit == 112.99998084763949
    assert best_invest_strat.profit == 112.99998084763949
