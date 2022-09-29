from server.common.abstract import User
from typing import Optional
from server.db.user_db_impl import __add_new_user, __get_user_by_login


def add_new_user(user: User):
    return __add_new_user(user)


def get_user_by_login(login: str) -> Optional[User]:
    return __get_user_by_login(login)

