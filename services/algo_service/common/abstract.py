from pydantic import BaseModel
from typing import Dict, List
import datetime
from services.user_service.common.abstract import Restriction  # used in algo as well!!!


class InvestItem(BaseModel):
    name: str = ''
    country: str = ''
    id: str = ''
    date_from: datetime.date = datetime.date(1000, 1, 1)
    date_till: datetime.date = datetime.date(1000, 1, 1)
    history: List[float] = []


class InvestStrategy(BaseModel):
    profit: float = 0

    distribution: Dict[str, float] = dict()  # [0 .. 1] (= % / 100) For all CURRENT_INDEXES.
