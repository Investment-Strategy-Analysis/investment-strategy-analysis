import logging
from fastapi import FastAPI
from services.algo_service.common.consts import DATEFMT
from services.algo_service.common.abstract import Restriction
from services.algo_service.algorithm.algorithm_api import get_solutions

logging.basicConfig(format='%(asctime)s.%(msecs)03dZ %(name)s %(levelname)s %(message)s',
                    datefmt=DATEFMT,
                    level=logging.INFO)

app = FastAPI()

# swagger - "http://0.0.0.0:8001/docs"


@app.get("/ping", summary="Return pong")
async def ping() -> str:
    """just return ping"""
    logging.info("ping")
    return "pong"


@app.post('/solutions', summary="Get solutions")
async def post_solutions(restriction: Restriction):
    return get_solutions(restriction)
