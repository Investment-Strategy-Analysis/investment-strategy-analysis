import pytest as pytest
import sys

from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import save_user, get_user_by_login
from services.user_service.db.user_db_impl import delete_user_by_login

sys.path.append('C:\\Users\\mozha\\HOMEWORK\\7sem\\PI\\investment-strategy-analysis')

test_data_one_user = [
    User(login="new_login", password="qwerty"),
]

test_data_few_users = [
    (User(login="a1", password="qwerty"), User(login="a2", password="qwerty"), User(login="a3", password="qwerty123")),
]


@pytest.mark.parametrize("u1", test_data_one_user)
def test_delete_user(u1):
    save_user(u1)
    assert get_user_by_login(u1.login) == u1
    delete_user_by_login(u1.login)
    assert get_user_by_login(u1.login) == None


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_delete_few_users(u1, u2, u3):
    save_user(u1)
    save_user(u2)
    save_user(u3)
    assert get_user_by_login(u1.login) == u1
    delete_user_by_login(u2.login)
    delete_user_by_login(u1.login)
    assert get_user_by_login(u1.login) == None


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_delete_nonexistent_users(u1, u2, u3):
    delete_user_by_login(u2.login)
    delete_user_by_login(u1.login)
    assert get_user_by_login(u1.login) == None
