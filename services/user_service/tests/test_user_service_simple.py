import pytest
from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import save_user, get_user_by_login, delete_user_by_login

test_data_one_user = [
    User(login="new_login", password="qwerty"),
]


@pytest.mark.parametrize("user", test_data_one_user)
def test_add_get_one_user(user):
    save_user(user)
    user_from_db = get_user_by_login(user.login)
    assert user_from_db.login == user.login


test_data_few_users = [
    (User(login="a1", password="qwerty"), User(login="a2", password="qwerty"), User(login="a3", password="qwerty123")),
]


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_get_few_users(u1, u2, u3):
    save_user(u1)
    save_user(u2)
    save_user(u3)
    assert get_user_by_login(u1.login).login == u1.login
    assert get_user_by_login(u2.login).login == u2.login
    assert get_user_by_login(u3.login).login == u3.login
    delete_user_by_login(u1.login)
    delete_user_by_login(u2.login)
    delete_user_by_login(u3.login)


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_get_unregistered_users(u1, u2, u3):
    save_user(u1)
    save_user(u2)
    assert get_user_by_login(u1.login).login == u1.login
    assert get_user_by_login(u2.login).login == u2.login
    assert get_user_by_login(u3.login) == None
    delete_user_by_login(u1.login)
    delete_user_by_login(u2.login)


@pytest.mark.parametrize("u1, u2, u3", test_data_few_users)
def test_add_same_users(u1, u2, u3):
    try:
        save_user(u1)
        save_user(u1)
    except Exception as e:
        delete_user_by_login(u1.login)
        return
    assert "Same user saved twice"
    delete_user_by_login(u1.login)
