import pytest as pytest
import sys

from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import add_new_user, get_user_by_login

sys.path.append('C:\\Users\\mozha\\HOMEWORK\\7sem\\PI\\investment-strategy-analysis')

test_data_one_user = [
    User(login="new_login", password="qwerty"),
]


@pytest.mark.parametrize("user", test_data_one_user)
def test_add_get_one_user(user):
    add_new_user(user)
    assert get_user_by_login(user.login) == user


test_data_few_users = [
    (User(login="a1", password="qwerty"), User(login="a2", password="qwerty"), User(login="a3", password="qwerty123")),
]


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_get_few_users(u1, u2, u3):
    add_new_user(u1)
    add_new_user(u2)
    add_new_user(u3)
    assert get_user_by_login(u1.login) == u1
    assert get_user_by_login(u2.login) == u2
    assert get_user_by_login(u3.login) == u3


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_get_unregistered_users(u1, u2, u3):
    add_new_user(u1)
    add_new_user(u2)
    assert get_user_by_login(u1.login) == u1
    assert get_user_by_login(u2.login) == u2
    assert get_user_by_login(u3.login) == None


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_same_users(u1, u2, u3):
    add_new_user(u1)
    add_new_user(u3)
    add_new_user(u1)
    add_new_user(u3)
    add_new_user(u1)
    assert get_user_by_login(u1.login) == u1
    assert get_user_by_login(u2.login) == None
    assert get_user_by_login(u3.login) == u3
