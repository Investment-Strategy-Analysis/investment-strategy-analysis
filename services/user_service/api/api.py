import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services.user_service.business_logic as bl
from services.user_service.common.abstract import *
from services.user_service.common.consts import DATEFMT

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


@app.get("/user")
async def get_user(login: str) -> User:
    """get user by login"""
    logging.info("execute raw")
    return await bl.get_user(login)


@app.post("/user")
async def post_user(user: User):
    """post user"""
    logging.info("execute raw")
    await bl.post_user(user)
