import logging
from services.user_service.common.abstract import User
from services.user_service.db.user_db_api import add_new_user as __add_new_user
from services.user_service.db.user_db_api import get_user_by_login as __get_user_by_login


async def post_user(user: User):
    logging.info(f"add user with login {user.login}")
    __add_new_user(user)


async def get_user(login: str) -> User:
    return __get_user_by_login(login)
