from services.user_service.common.abstract import User, Email, Password, Photo, Settings, UserSettings
from services.user_service.db.user_db_impl import save_user as __save_user
from services.user_service.db.user_db_impl import update_settings as __update_settings
from services.user_service.db.user_db_impl import update_user_settings as __update_user_settings
from services.user_service.db.user_db_impl import update_user_email as __update_user_email
from services.user_service.db.user_db_impl import update_user_password as __update_user_password
from services.user_service.db.user_db_impl import update_user_photo as __update_user_photo
from services.user_service.db.user_db_impl import get_user_by_login as __get_user_by_login
from services.user_service.db.user_db_impl import delete_user_by_login as __delete_user_by_login


def save_user(user: User):  # if it's a new user creates it.
    return __save_user(user)


def update_settings(login: str, settings: Settings):
    return __update_settings(login, settings)


def update_user_settings(login: str, user_settings: UserSettings):
    return __update_user_settings(login, user_settings)


def update_user_email(login: str, email: Email):
    return __update_user_email(login, email)


def update_user_password(login: str, password: Password):
    return __update_user_password(login, password)


def update_user_photo(login: str, photo: Photo):
    return __update_user_photo(login, photo)


def get_user_by_login(login: str) -> User:
    return __get_user_by_login(login)


def delete_user_by_login(login: str):
    return __delete_user_by_login(login)
