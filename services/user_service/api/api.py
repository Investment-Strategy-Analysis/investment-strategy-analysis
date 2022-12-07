import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from typing import Tuple
import services.user_service.business_logic as bl
from services.user_service.common.abstract import *
from services.user_service.common.consts import DATEFMT, OK
from services.user_service.api.authorization.deps import get_current_user, refresh_tokens
from services.user_service.common.helpers import post
from services.user_service.common.endpoints import *
from deprecated import deprecated
from services.common.singletons import STRATEGIES

logging.basicConfig(format='%(asctime)s.%(msecs)03dZ %(name)s %(levelname)s %(message)s',
                    datefmt=DATEFMT,
                    level=logging.INFO)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# swagger - "http://0.0.0.0:8000/docs"


@app.get("/", summary="Show all operations and their descriptions")
async def get_operations(user: User = Depends(get_current_user)) -> dict[str, dict[str, str]]:
    logging.info(f"{user.login} get operations")
    operations = [ping, get_user, get_token_refresh, get_settings, get_current_settings, get_user_settings, post_tokens, 
                  post_user, post_settings, post_settings_add, post_user_parameters, post_user_email, 
                  post_user_password, post_user_photo, delete_user, get_analysis_times, get_checkboxes, get_strategies, post_solutions]
    return {"Operations": dict(map(lambda x: (x.__name__, x.__doc__), operations))}


@app.get("/ping", summary="Return pong")
async def ping() -> str:
    """just return ping"""
    logging.info("ping")
    return "pong"


@app.get("/user", summary="Return current user", response_model=User)
async def get_user(user: User = Depends(get_current_user)) -> User:
    """get user by login"""
    user.password = ""      # not show
    logging.info("get user")
    return user


@app.get("/token/refresh", summary="refresh tokens")
async def get_token_refresh(tokens: Tokens = Depends(refresh_tokens)) -> Tokens:
    """refresh tokens"""
    return tokens


@app.get("/user/settings", summary="Return settings")
async def get_settings(user: User = Depends(get_current_user)) -> List[Settings]:
    """return settings"""
    return user.settings


@app.get("/user/current_settings", summary="Return current_settings")
async def get_current_settings(user: User = Depends(get_current_user)) -> Settings:
    """return current_settings"""
    return user.current_settings


@app.get("/user/user_settings", summary="Return user_settings")
async def get_user_settings(user: User = Depends(get_current_user)) -> UserSettings:
    """return user_settings"""
    return user.user_settings


@app.post('/login', summary="Create access and refresh tokens for user")
async def post_tokens(data: OAuth2PasswordRequestForm = Depends()) -> Tokens:
    """just login OAuth2"""
    return await bl.post_tokens(data)


@app.post("/user", summary="Create new user, settings=[]")
async def post_user(user: User):
    """post user"""
    logging.info(f"try post user {user.login}")
    await bl.post_user(user)
    return OK


# @app.post("/user/current_settings", summary="Update current settings for current user")
async def post_current_settings(settings: Settings, user: User = Depends(get_current_user)):
    """update current settings for current user"""
    logging.info("update user current_settings")
    await bl.update_current_settings(user, settings)
    return OK


@app.post("/user/settings", summary="Reset all settings for current user")
async def post_settings(settings: List[Settings], user: User = Depends(get_current_user)):
    """reset all settings for current user"""
    logging.info("reset user settings")
    await bl.reset_settings(user, settings)
    return OK


@app.post("/user/settings/add", summary="Save current settings to settings")
async def post_settings_add(user: User = Depends(get_current_user)):
    """save current settings to settings"""
    logging.info("add current_settings to settings for current user")
    await bl.save_from_current_settings(user)
    return OK


@deprecated(version='1', reason="Use more specific /user/photo, /user/email, ...")
@app.post("/user/parameters", summary="Update parameters for current user, deprecated (Use more specific /user/photo, /user/email, ...)")
async def post_user_parameters(user_settings: UserSettings, user: User = Depends(get_current_user)):
    """update parameters for current user"""
    logging.info("update user parameters")
    await bl.update_user_parameters(user, user_settings)
    return OK


@app.post("/user/email", summary="Update email for current user")
async def post_user_email(email: Email, user: User = Depends(get_current_user)):
    """update email for current user"""
    logging.info("update user email")
    await bl.update_user_email(user, email)
    return OK


@app.post("/user/password", summary="Update password for current user")
async def post_user_password(password: Password, user: User = Depends(get_current_user)):
    """update password for current user"""
    logging.info("update user password")
    await bl.update_user_password(user, password)
    return OK


@app.post("/user/photo", summary="Update photo for current user")
async def post_user_photo(photo: Photo, user: User = Depends(get_current_user)):
    """update photo for current user"""
    logging.info("update user photo")
    await bl.update_user_photo(user, photo)
    return OK


@app.delete("/user", summary="Delete current user")
async def delete_user(user: User = Depends(get_current_user)):
    """delete current user"""
    logging.info("delete user")
    await bl.delete_user(user)
    return OK


### algorithm
@deprecated(reason="use numbers in analysis_times field")
@app.get('/settings/analysis_times', summary="show possible analysis times (deprecated)")
async def get_analysis_times() -> AnyList:  # data=[int]
    """get possible analysis times"""
    return AnyList(data=[])


@app.get('/settings/checkboxes', summary="show possible checkboxes")
async def get_checkboxes() -> AnyList:      # data=[CheckboxInfo]
    """get possible checkboxes"""
    return AnyList(data=[checkbox.value for checkbox in Checkbox])


@app.get('/settings/strategies', summary="show possible strategies")
async def get_strategies() -> AnyList:      # data=[InvestStrategy]
    """get possible strategies"""
    return AnyList(data=list(STRATEGIES.values()))


# connectors (also without auth later)
@app.post('/solutions', summary="Get solutions")
async def post_solutions(restriction: Restriction, user: User = Depends(get_current_user)) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    logging.info(f"solutions, {user.login}")
    settings = Settings(restrictions=restriction)
    await post_current_settings(settings, user)
    return await post(SOLUTIONS, restriction.json())
