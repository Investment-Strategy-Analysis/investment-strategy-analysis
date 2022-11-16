import pytest
from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import save_user, get_user_by_login


@pytest.mark.parametrize(
    "a, b, c",
    [
        (2, 2, 4),
        (1, 2, 3),
    ]
)
def test_simple(a, b, c):
    assert a + b == c


test_data_one_user = [
    User(login="new_login", password="qwerty"),
]


@pytest.mark.parametrize("user", test_data_one_user)
def test_add_get_one_user(user):
    save_user(user)
    assert get_user_by_login(user.login) == user

