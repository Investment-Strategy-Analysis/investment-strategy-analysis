import pytest
from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import save_user, get_user_by_login


test_data_one_user = [
    User(login="new_login", password="qwerty"),
]


@pytest.mark.parametrize("user", test_data_one_user)
def test_add_get_one_user(user):
    save_user(user)
    user_from_db = get_user_by_login(user.login)
    assert user_from_db.login == user.login
