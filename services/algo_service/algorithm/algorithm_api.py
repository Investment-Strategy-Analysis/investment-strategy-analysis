from typing import List, Tuple
from services.algo_service.common.abstract import Restriction, InvestStrategy, Index, Checkbox, AnalysisTime
from services.algo_service.algorithm.algorithm_impl import get_solutions as __get_solutions


# returns the best solution and all found


def get_solutions(restriction: Restriction) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    return __get_solutions(restriction)


def example_test():
    best, front = get_solutions(Restriction(target_profit=13,
                                            checkboxes={checkbox.name: False for checkbox in Checkbox},
                                            upper_border={index.name: 1 for index in Index},
                                            lower_border={index.name: 0 for index in Index},
                                            analysis_time=100))
    print(best)
    print(front)


if __name__ == '__main__':
    example_test()
