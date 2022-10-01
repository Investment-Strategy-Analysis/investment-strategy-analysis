import logging
from fastapi import FastAPI
from services.algo_service.common.consts import DATEFMT
from services.algo_service.common.abstract import AlgorithmParams
from services.algo_service.algorithm.algorithm_api import get_some_solutions, get_best_solution

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


@app.post('/solutions', summary="Get some solutions")
async def post_solutions(params: AlgorithmParams):
    logging.info(f"solutions, {params.login}")
    return get_some_solutions(params.restriction)


@app.post('/best_solutions', summary="Get best solutions")
async def post_best_solutions(params: AlgorithmParams):
    logging.info(f"best_solutions, {params.login}")
    return get_best_solution(params.restriction)
