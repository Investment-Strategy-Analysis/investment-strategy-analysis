from services.user_service.common.abstract import User
from services.user_service.db.user_db_impl import add_new_user as __add_new_user
from services.user_service.db.user_db_impl import get_user_by_login as __get_user_by_login


def add_new_user(user: User):
    return __add_new_user(user)


def get_user_by_login(login: str) -> User:
    return __get_user_by_login(login)

