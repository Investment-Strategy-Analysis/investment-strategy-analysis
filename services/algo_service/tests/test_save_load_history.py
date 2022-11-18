import pytest

from services.algo_service.db.data_db_api import save_history, load_history
from services.algo_service.db.tables import InvestItem


test_data_few_users = [
    InvestItem(name='t1', country='q', id='id', history=[1]),
]


@pytest.mark.parametrize("a", test_data_few_users)
def test_save_history(a):
    save_history(a)
    b = load_history(a)
    assert a.id == b.id
