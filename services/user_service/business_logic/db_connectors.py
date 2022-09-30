from services.user_service.common.abstract import User, Settings, UserSettings
from services.user_service.db.user_db_api import save_user as __add_new_user
from services.user_service.db.user_db_api import get_user_by_login as __get_user_by_login


async def get_user(login: str) -> User:
    return __get_user_by_login(login)


async def post_user(user: User):
    __add_new_user(user)


async def update_user_settings(login: str, settings: Settings):
    user = __get_user_by_login(login)
    user.settings = settings
    __add_new_user(user)


async def update_user_parameters(login: str, user_settings: UserSettings):
    user = __get_user_by_login(login)
    user.user_settings = user_settings
    __add_new_user(user)


async def delete_user(login: str):
    pass
