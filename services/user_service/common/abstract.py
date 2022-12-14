from typing import Any, Optional, List
from pydantic import BaseModel
from services.common.abstract import *

class Email(BaseModel):
    email: str


class Password(BaseModel):
    password: str


class Photo(BaseModel):
    photo: bytes


class Settings(BaseModel):
    strategy: str = "default"
    # checkboxes - We need to do function that gives us Restriction.upper_border and Restriction.lower_border from this
    restrictions: Restriction = Restriction()
    risk: float = 0
    # other


class LastAnswer(BaseModel):
    result: Optional[List[float]] = None
    settings: Optional[Settings] = None


class UserSettings(BaseModel):
    last_answer: Optional[LastAnswer] = None
    photo: Optional[bytes] = None
    email: Optional[str] = None
    # other extra info


class User(BaseModel):
    login: str      # id
    password: str   # hash
    current_settings: Settings = Settings()
    settings: List[Settings] = []
    user_settings: UserSettings = UserSettings()


class TokenPayload(BaseModel):
    expires_delta: str
    login: str


class AlgorithmParams(BaseModel):
    restriction: Restriction


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class UsernamePassword(BaseModel):
    username: str
    password: str


class AnalyticItem(BaseModel):
    restriction: Restriction
    login: str
    datatime: str


class AnalyticQuery(BaseModel):
    query: Optional[Dict[str, Any]] = None
