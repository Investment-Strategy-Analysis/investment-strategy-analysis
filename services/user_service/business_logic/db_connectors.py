from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.user_service.common.abstract import User, Settings, UserSettings
from services.user_service.db.user_db_api import get_user_by_login as __get_user_by_login
from services.user_service.db.user_db_api import save_user as __save_user
from services.user_service.db.user_db_api import update_user as __update_user
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


async def post_tokens(data: OAuth2PasswordRequestForm):
    user = await get_user(data.username, check=True)
    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect login or password"
        )
    return {
        "access_token": create_access_token(user.login),
        "refresh_token": create_refresh_token(user.login),
    }


async def update_user_settings(user: User, settings: Settings):
    user.settings = settings
    return __update_user(user)


async def update_user_parameters(user: User, user_settings: UserSettings):
    user.user_settings = user_settings
    return __update_user(user)


async def delete_user(user: User):
    return __delete_user_by_login(user.login)
