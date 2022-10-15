from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy
from services.algo_service.algorithm.algorithm_impl import get_solutions as __get_solutions
from services.algo_service.common.consts import CHECKBOXES


# returns the best solution and all found


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    return __get_solutions(restriction)


def example_test():
    from services.algo_service.common.singletons import CURRENT_INDEXES
    best, front = get_solutions(Restriction(target_profit=13,
                                            checkboxes={i: False for i in CHECKBOXES},
                                            upper_border={i: 1 for i in CURRENT_INDEXES.keys()},
                                            lower_border={i: 0 for i in CURRENT_INDEXES.keys()},
                                            analysis_time=100))
    print(best)
    print(front)


if __name__ == '__main__':
    example_test()
