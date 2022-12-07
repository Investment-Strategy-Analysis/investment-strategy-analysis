import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_engine():
    username = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    db = os.environ.get("POSTGRES_DB")
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{db}:5432/{db}", echo=True)
    return engine


def db_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
