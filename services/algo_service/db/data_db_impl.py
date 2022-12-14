from services.algo_service.common.abstract import InvestItem
import logging
from services.algo_service.common.helpers import db_engine, db_session
from services.algo_service.db.tables import Base
import services.algo_service.db.tables as T
from typing import Optional

__engine = db_engine()
session = db_session(__engine)
Base.metadata.create_all(__engine)  # create tables if not exists


def save_history(item: InvestItem):
    invest_item = session.query(T.InvestItem).filter(T.InvestItem.id == item.id).first()
    if invest_item is None:
        invest_item = T.InvestItem(id=item.id, name=item.name, country=item.country, date_from=item.date_from, date_till=item.date_till, history=item.history)
    else:
        invest_item.name = item.name
        invest_item.country = item.country
        invest_item.date_from = item.date_from
        invest_item.date_till = item.date_till
        invest_item.history = item.history
    session.add(invest_item)
    session.commit()
    logging.info(f'Saved history: {invest_item.id}')


def load_history(item_id: str) -> Optional[InvestItem]:
    invest_item = session.query(T.InvestItem).filter(T.InvestItem.id == item_id).first()
    if invest_item is None:
        return None
    return invest_item.to_pydantic()
