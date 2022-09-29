from server.common.abstract import User
from typing import Optional
import sqlite3
import logging


file_db_name = 'LoginDB.db'
table_name = 'login'
singleton_database = None
singleton_cursor = None


def check_db_not_none():
    global singleton_database, singleton_cursor
    if singleton_database is None:
        singleton_database = sqlite3.connect(file_db_name)
        singleton_cursor = singleton_database.cursor()
        singleton_cursor.execute(
'CREATE TABLE IF NOT EXISTS {}(login, password_hash, restriction, last_answer, timestamp)'.format(table_name))
        singleton_database.commit()


def get_vals(item: User):
    return f"'{item.login}', '{item.password_hash}', '{str(item.restriction)}', '{item.last_answer}', '{item.timestamp}'"


def parse_user(item: list) -> User:
    return User()


def add_new_user(user: User):
    global singleton_database, singleton_cursor
    check_db_not_none()
    logging.info(f'Added in {table_name} user: {user.login}.')
    singleton_cursor.execute(f'INSERT INTO {table_name} VALUES ({get_vals(user)})')
    singleton_database.commit()


def get_user_by_login(login: str) -> Optional[User]:
    global singleton_database, singleton_cursor
    check_db_not_none()
    users = singleton_cursor.execute(f'SELECT * FROM {table_name} WHERE login = {login}').fetchall()
    if len(users) == 0:
        return None
    else:
        return parse_user(users[0])
