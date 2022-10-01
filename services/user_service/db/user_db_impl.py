from typing import Optional
from services.user_service.common.abstract import User
from sqlitedict import SqliteDict
import logging


file_db_name = 'LoginDB.db'
singleton_database = None


def get_db():
    global singleton_database
    if singleton_database is None:
        singleton_database = SqliteDict(file_db_name, autocommit=True)
    return singleton_database


def save_user(user: User):
    db = get_db()
    db[user.login] = user
    logging.info(f'Saved user: {user.login}.')


def get_user_by_login(login: str) -> Optional[User]:
    db = get_db()
    if login in db.keys():
        result = db[login]
        if result != 'deleted':
            return result
        else:
            return None
    else:
        return None


def delete_user_by_login(login: str):
    db = get_db()
    db[login] = 'deleted'
    logging.info(f'Deleted user: {login}.')
