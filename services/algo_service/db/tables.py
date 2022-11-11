import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, ARRAY, Float, Date, String
from sqlalchemy.orm import declarative_base
import services.algo_service.common.abstract as A


class BasePydantic:
    def to_pydantic(self):
        pass


Base = declarative_base(cls=BasePydantic)


def _get_pydantic(base_obj: Optional[BasePydantic]) -> Optional[BaseModel]:
    if base_obj is None:
        return None
    return base_obj.to_pydantic()


class InvestItem(Base):
    __tablename__ = "invest_items"
    id = Column(String, primary_key=True)
    date_from = Column("date_from", Date, nullable=False, default=datetime.date(1000, 1, 1))
    date_till = Column("date_till", Date, nullable=False, default=datetime.date(1000, 1, 1))
    history = Column("lower_border", ARRAY(Float, dimensions=1), nullable=False, default=[])

    def __repr__(self):
        return f"InvestItem(id={self.id}, date_from={self.date_from}, date_till={self.date_till}, " \
               f"history={self.history})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        return A.InvestItem(date_from=self.date_from, date_till=self.date_till, history=self.history)
