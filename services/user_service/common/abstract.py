from typing import Optional, List, Dict
from pydantic import BaseModel


class Settigns(BaseModel):
    strategy: str = "default"
    restrictions: Dict[str, float] = dict()
    period: str = "year"
    probability: float = 1
    risk: float = 0
    # other


class lastAnswer(BaseModel):
    result: Optional[List[float]] = None
    settings: Optional[Settigns] = None


class UserSettigns(BaseModel):
    last_answer: lastAnswer = lastAnswer()
    photo: Optional[bytes] = None
    email: Optional[str] = None
    # other extra info


class User(BaseModel):
    login: str      # id
    password: str   # hash
    settings: Settigns = Settigns()
    user_settings: UserSettigns = UserSettigns()
