from services.algo_service.common.abstract import InvestItem
from sqlitedict import SqliteDict
import logging


file_db_name = 'DataDB.db'
singleton_database = None


def get_db():
    global singleton_database
    if singleton_database is None:
        singleton_database = SqliteDict(file_db_name, autocommit=True)
    return singleton_database


def save_history(item: InvestItem):
    db = get_db()
    db[item.id] = item.history.data
    logging.info(f'Saved history: {item.id}.')


def load_history(item: InvestItem) -> InvestItem:
    item.history.data = None
    db = get_db()
    if item.id in db.keys():
        result = db[item.id]
        if result != 'deleted':
            item.history.data = result
    return item


def delete_history(item: InvestItem):
    item.history.data = None
    db = get_db()
    db[item.id] = 'deleted'
    logging.info(f'Deleted history: {item.id}.')
