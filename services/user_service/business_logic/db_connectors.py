from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Union, List
from services.user_service.common.abstract import User, Settings, UserSettings, Email, Password, Photo, Tokens, UsernamePassword
from services.user_service.db.user_db_api import get_user_by_login as __get_user_by_login
from services.user_service.db.user_db_api import save_user as __save_user
from services.user_service.db.user_db_api import reset_settings as __reset_settings
from services.user_service.db.user_db_api import save_from_current_settings as __save_from_current_settings
from services.user_service.db.user_db_api import update_current_settings as __update_current_settings
from services.user_service.db.user_db_api import update_user_settings as __update_user_settings
from services.user_service.db.user_db_api import update_user_email as __update_user_email
from services.user_service.db.user_db_api import update_user_password as __update_user_password
from services.user_service.db.user_db_api import update_user_photo as __update_user_photo
from services.user_service.db.user_db_api import delete_user_by_login as __delete_user_by_login
from services.user_service.api.authorization.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token


async def get_user(login: str, check=False) -> User:
    user = __get_user_by_login(login)
    if check and user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this login not exist"
        )
    return user


async def post_user(user: User):
    __user = await get_user(user.login)
    if __user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this login already exist"
        )
    user.password = get_hashed_password(user.password)
    return __save_user(user)


async def post_tokens(data: Union[OAuth2PasswordRequestForm, UsernamePassword], pass_hashed: bool = False) -> Tokens:
    user = await get_user(data.username, check=True)
    if not verify_password(data.password, user.password, pass_hashed=pass_hashed):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect login or password"
        )
    return Tokens(access_token=create_access_token(user.login), refresh_token=create_refresh_token(user.login))


async def save_from_current_settings(user: User):
    return __save_from_current_settings(user.login)


async def reset_settings(user: User, settings: List[Settings]):
    return __reset_settings(user.login, settings)


async def update_current_settings(user: User, settings: Settings):
    return __update_current_settings(user.login, settings)


async def update_user_parameters(user: User, user_settings: UserSettings):
    return __update_user_settings(user.login, user_settings)


async def update_user_email(user: User, email: Email):
    return __update_user_email(user.login, email)


async def update_user_password(user: User, password: Password):
    return __update_user_password(user.login, password)


async def update_user_photo(user: User, photo: Photo):
    return __update_user_photo(user.login, photo)


async def delete_user(user: User):
    return __delete_user_by_login(user.login)
