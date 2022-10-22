from pydantic import BaseModel
from typing import Dict, List, Optional
import datetime


class InvestItem(BaseModel):
    name: str = ''
    country: str = ''
    id: Optional[str] = None
    date_from: datetime.date = datetime.date(1000, 1, 1)
    date_till: datetime.date = datetime.date(1000, 1, 1)
    history: List[float] = []


class InvestStrategy(BaseModel):
    profit: float = 0
    risk: float = 0
    distribution: Dict[str, float] = dict()  # [0 .. 1] (= % / 100) For all CURRENT_INDEXES.


# copy-paste from user-service
class Restriction(BaseModel):
    target_profit: float = 0  # used to find best point in pareto front
    checkboxes: Dict[str, bool] = dict()     # true/false For all checkboxes.
    upper_border: Optional[Dict[str, float]] = None  # [0 .. 1] less then. For all CURRENT_INDEXES.
                                                     # Or None if it isn't advanced request.
    lower_border: Optional[Dict[str, float]] = None  # [0 .. 1] more then. For all CURRENT_INDEXES.
                                                     # Or None if it isn't advanced request.
    analysis_time: int = 0                     # how many days to analyse
