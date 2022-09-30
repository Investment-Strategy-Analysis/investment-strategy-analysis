from typing import Optional, List, Dict
from pydantic import BaseModel


class Settings(BaseModel):
    strategy: str = "default"
    checkboxes: Dict[str, bool] = dict()
    restrictions: Dict[str, float] = dict()
    period: str = "year"
    probability: float = 1
    risk: float = 0
    # other


class LastAnswer(BaseModel):
    result: Optional[List[float]] = None
    settings: Optional[Settings] = None


class UserSettings(BaseModel):
    last_answer: LastAnswer = LastAnswer()
    photo: Optional[bytes] = None
    email: Optional[str] = None
    # other extra info


class User(BaseModel):
    login: str      # id
    password: str   # hash
    settings: Settings = Settings()
    user_settings: UserSettings = UserSettings()
