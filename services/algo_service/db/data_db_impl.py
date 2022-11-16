from services.algo_service.common.abstract import InvestItem
import logging
from services.algo_service.common.helpers import db_engine, db_session
from services.algo_service.db.tables import Base
import services.algo_service.db.tables as T

__engine = db_engine()
__session = db_session(__engine)
Base.metadata.create_all(__engine)  # create tables if not exists


def save_history(item: InvestItem):
    if item.id is not None:
        invest_item = __session.query(T.InvestItem).filter(T.InvestItem.id == item.id).first()
        invest_item.date_from = item.date_from
        invest_item.date_till = item.date_till
        invest_item.history = item.history
    else:
        invest_item = T.InvestItem(date_from=item.date_from, date_till=item.date_till, history=item.history)
    __session.add(invest_item)
    __session.commit()
    logging.info(f'Saved history: {invest_item.id}')


def load_history(item_id: str) -> InvestItem:
    invest_item = __session.query(T.InvestItem).filter(T.InvestItem.id == item_id).first()
    return invest_item.to_pydantic()
