from pydantic import BaseModel
from typing import Dict, List
import datetime


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


# copy-paste from user-service
class Restriction(BaseModel):   # used in algo as well!!!
    target_profit: float = 0  # used to find best point in pareto front
    upper_border: Dict[str, float] = dict()  # [0 .. 1] less then. For all CURRENT_INDEXES
    lower_border: Dict[str, float] = dict()  # [0 .. 1] more then. For all CURRENT_INDEXES
    analysis_time: int = 0                     # how many days to analyse
