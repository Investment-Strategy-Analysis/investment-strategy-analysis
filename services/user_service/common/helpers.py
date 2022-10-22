import os
import aiohttp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.user_service.common.consts import AIOHTTP_TIMEOUT, HEADERS


async def post(path: str, data: str):
    async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
        async with session.post(path, data=data, headers=HEADERS) as response:
            return await response.json()


def db_engine():
    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@user-db:5432/user_db", echo=True)
    return engine


def db_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
