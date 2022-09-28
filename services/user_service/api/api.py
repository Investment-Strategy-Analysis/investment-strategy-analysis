import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services.user_service.business_logic as bl
from services.user_service.common.abstract import *
from services.user_service.common.consts import DATEFMT, OK

logging.basicConfig()
logging.basicConfig(format='%(asctime)s.%(msecs)03dZ %(name)s %(levelname)s %(message)s',
                    datefmt=DATEFMT,
                    level=logging.INFO)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5001",
    "http://0.0.0.0:5001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# swagger - "http://0.0.0.0:8000/docs"


@app.get("/")
async def get_operations() -> dict[str, dict[str, str]]:
    operations = [ping, get_user, post_user]
    return {"Operations": dict(map(lambda x: (x.__name__, x.__doc__), operations))}


@app.get("/ping")
async def ping() -> str:
    """just return ping"""
    logging.info("ping")
    return "pong"


@app.get("/user/{login}")
async def get_user(login: str) -> User:
    """get user by login"""
    logging.info("get user")
    user = await bl.get_user(login)
    if user is None:
        error = f"User with login={login} not found"
        logging.error(error)
        return error      # remove later
    return user


@app.post("/user")
async def post_user(user: User):
    """post user"""
    logging.info("post user")
    await bl.post_user(user)
    return OK


@app.post("/user/{login}/settings")
async def post_user_settings(login: str, settings: Settings):
    """post user"""
    logging.info("update user settings")
    await bl.update_user_settings(login, settings)
    return OK


# TODO(more detail?)
@app.post("/user/{login}/parameters")
async def post_user_parameters(login: str, user_settings: UserSettings):
    """post user"""
    logging.info("update user parameters")
    await bl.update_user_parameters(login, user_settings)
    return OK


@app.delete("/user/{login}")
async def delete_user(login: str):
    """delete user"""
    logging.info("delete user")
    await bl.delete_user(login)
    return OK
