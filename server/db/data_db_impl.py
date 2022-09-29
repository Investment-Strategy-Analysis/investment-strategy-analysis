from typing import List
import sqlite3
import logging
from server.abstract import OperationWithInfo


file_db_name = 'DataDB.db'
table_name = 'data'
singleton_database = None
singleton_cursor = None


def check_db_not_none():
    global singleton_database, singleton_cursor
    if singleton_database is None:
        singleton_database = sqlite3.connect(file_db_name)
        singleton_cursor = singleton_database.cursor()
        singleton_cursor.execute('CREATE TABLE IF NOT EXISTS {}(data, result, success, timestamp)'.format(table_name))
        singleton_database.commit()


def __get_history() -> List[OperationWithInfo]:
    global singleton_database, singleton_cursor
    check_db_not_none()
    dicts = singleton_cursor.execute('SELECT * FROM ' + table_name).fetchall()
    items = []
    for i in dicts:
        items.append(OperationWithInfo(data=i[0], result=i[1], success=int(i[2]), timestamp=i[3]))
    return items


def get_vals(item: OperationWithInfo):
    return f"'{item.data}', '{item.result}', '{str(item.success)}', '{item.timestamp}'"


def __put_new_record(item: OperationWithInfo):
    global singleton_database, singleton_cursor
    check_db_not_none()
    logging.info(f'INSERT INTO {table_name} VALUES ({get_vals(item)})')
    singleton_cursor.execute(f'INSERT INTO {table_name} VALUES ({get_vals(item)})')
    singleton_database.commit()