import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_engine():
    username = os.environ.get("DB_USER")
    password = os.environ.get("ALGO_DB_PASSWORD")
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@algo-db:5432/algo_db", echo=True)
    return engine


def db_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
