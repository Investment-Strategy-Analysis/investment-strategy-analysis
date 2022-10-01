from services.algo_service.common.abstract import InvestItem
from services.algo_service.db.data_db_impl import save_history as __save_history
from services.algo_service.db.data_db_impl import load_history as __load_history
from services.algo_service.db.data_db_impl import delete_history as __delete_history


def save_history(item: InvestItem):  # if it's a new user creates it.
    return __save_history(item)


def load_history(item: InvestItem) -> InvestItem:
    return __load_history(item)


def delete_history(item: InvestItem):
    return __delete_history(item)


def __small_example():
    a = InvestItem(name='name', country='country', id='id')
    print(a.history.data)
    a.history.data = [1]
    print(a.history.data)
    save_history(a)
    print(a.history.data)
    a.history.data = [2]
    print(a.history.data)
    load_history(a)
    print(a.history.data)
    delete_history(a)
    print(a.history.data)
    load_history(a)
    print(a.history.data)


if __name__ == '__main__':
    __small_example()