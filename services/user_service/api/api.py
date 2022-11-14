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
from services.common.helpers import to_analysis_time
from services.common.singletons import STRATEGIES

logging.basicConfig(format='%(asctime)s.%(msecs)03dZ %(name)s %(levelname)s %(message)s',
                    datefmt=DATEFMT,
                    level=logging.INFO)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5001",
    "http://0.0.0.0:5001",
    "http://127.0.0.1:5001",
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
    operations = [ping, get_user, post_user, post_user_settings, post_user_parameters, delete_user]
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


@app.post('/login', summary="Create access and refresh tokens for user")
async def post_tokens(data: OAuth2PasswordRequestForm = Depends()) -> Tokens:
    return await bl.post_tokens(data)


@app.post("/user", summary="Create new user")
async def post_user(user: User):
    """post user"""
    logging.info(f"try post user {user.login}")
    await bl.post_user(user)
    return OK


@app.post("/user/settings", summary="Update settings for current user")
async def post_user_settings(settings: Settings, user: User = Depends(get_current_user)):
    """update settings for current user"""
    logging.info("update user settings")
    await bl.update_user_settings(user, settings)
    return OK


@deprecated(version='1', reason="Use more specific /user/photo, /user/email, ...")
@app.post("/user/parameters", summary="Update parameters for current user")
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
@app.get('/settings/analysis_times', summary="show possible analysis times")
async def get_analysis_times() -> AnyList:  # data=[AnalysisTimeInfo]
    return AnyList(data=[time.value for time in AnalysisTime])


@app.get('/settings/checkboxes', summary="show possible checkboxes")
async def get_checkboxes() -> AnyList:      # data=[CheckboxInfo]
    return AnyList(data=[checkbox.value for checkbox in Checkbox])


@app.get('/settings/strategies', summary="show possible strategies")
async def get_strategies() -> AnyList:      # data=[InvestStrategy]
    return AnyList(data=list(STRATEGIES.values()))


# connectors (also without auth later)
@app.post('/solutions', summary="Get solutions")
async def post_solutions(restriction: Restriction, user: User = Depends(get_current_user)) -> Tuple[InvestStrategy, List[InvestStrategy]]:
    logging.info(f"solutions, {user.login}")
    if isinstance(restriction.analysis_time, str):
        restriction.analysis_time = to_analysis_time(restriction.analysis_time).value.days
    return await post(SOLUTIONS, restriction.json())
