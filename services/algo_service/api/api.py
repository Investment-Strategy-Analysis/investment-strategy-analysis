import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from services.algo_service.common.consts import DATEFMT
from services.algo_service.common.abstract import Restriction
from services.algo_service.algorithm.algorithm_api import get_solutions

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

# swagger - "http://0.0.0.0:8001/docs"


@app.get("/ping", summary="Return pong")
async def ping() -> str:
    """just return ping"""
    logging.info("ping")
    return "pong"


@app.post('/solutions', summary="Get solutions")
async def post_solutions(restriction: Restriction):
    return get_solutions(restriction)
