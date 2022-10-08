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
    db[item.id] = (item.date_from, item.date_till, item.history)
    logging.info(f'Saved history: {item.id}.')


def load_history(item: InvestItem) -> InvestItem:
    db = get_db()
    if item.id in db.keys():
        (item.date_from, item.date_till, item.history) = db[item.id]
    return item
