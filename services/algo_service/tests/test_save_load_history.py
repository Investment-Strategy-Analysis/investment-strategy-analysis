import pytest

from services.algo_service.db.data_db_api import save_history, load_history
from services.algo_service.db.tables import InvestItem


test_data_few_users = [
    InvestItem(),
]


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_save_history():
    a = InvestItem(name='t1', country='q', id='id', history=[1])
    print("InvestItem crated")
    save_history(a)
    print("InvestItem saved")
    b = load_history(a)
    print("InvestItem loaded")
    assert a.id == b.id
