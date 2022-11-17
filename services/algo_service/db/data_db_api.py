from services.algo_service.common.abstract import InvestItem
from services.algo_service.db.data_db_impl import save_history as __save_history
from services.algo_service.db.data_db_impl import load_history as __load_history


def save_history(item: InvestItem):
    return __save_history(item)


def load_history(item: InvestItem) -> InvestItem:
    return __load_history(item.id)
