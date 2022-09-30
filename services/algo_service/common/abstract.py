from pydantic import BaseModel
from typing import Optional, List


class InvestItemHistory(BaseModel):
    data: Optional[List[float]] = None


class InvestItem(BaseModel):
    name: str
    country: str
    id: str
    history: InvestItemHistory = InvestItemHistory()

