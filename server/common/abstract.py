from typing import Optional, List
from pydantic import BaseModel


class Restriction(BaseModel):
    upper_border: List[float]
    lower_border: List[float]
    granulation: float


class User(BaseModel):
    login: str
    password_hash: str
    restriction: Restriction
    last_answer: Optional[List[float]]
    timestamp: Optional[str]


class InvestItem(BaseModel):
    name: str
    country: str
    id: str
