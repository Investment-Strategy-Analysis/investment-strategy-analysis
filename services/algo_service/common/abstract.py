from pydantic import BaseModel
from typing import Optional, List
import datetime


class InvestItem(BaseModel):
    name: str = ''
    country: str = ''
    id: str = ''
    date_from: datetime.date = datetime.date(1000, 1, 1)
    date_till: datetime.date = datetime.date(1000, 1, 1)
    history: List[float] = []


class Restriction(BaseModel):  # ???
    pass


class AlgorithmParams(BaseModel):
    login: str
    restriction: Restriction
