import pytest

from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox
from services.algo_service.algorithm.algorithm_impl import get_solutions as __get_solutions


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    return __get_solutions(restriction)


test_data_restriction = [
    Restriction(target_profit=13,
                checkboxes={checkbox.value.id: False for checkbox in Checkbox},
                upper_border={index.value.id: 1 for index in Index},
                lower_border={index.value.id: 0 for index in Index},
                analysis_time=100),
]


@pytest.mark.parametrize("restrict", test_data_restriction)
def test_example(restrict):
    best, front = get_solutions(restrict)
    print(best)
    assert best == None
    print(front)
    assert front
