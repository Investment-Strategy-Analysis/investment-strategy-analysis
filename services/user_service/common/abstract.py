from typing import Optional, List, Dict
from pydantic import BaseModel


class Restriction(BaseModel):
    target_profit: float = 0  # used to find best point in pareto front
    checkboxes: Dict[str, bool] = dict()     # true/false For all checkboxes.
    upper_border: Optional[Dict[str, float]] = None  # [0 .. 1] less then. For all CURRENT_INDEXES.
                                                     # Or None if it isn't advanced request.
    lower_border: Optional[Dict[str, float]] = None  # [0 .. 1] more then. For all CURRENT_INDEXES.
                                                     # Or None if it isn't advanced request.
    analysis_time: int = 0                     # how many days to analyse


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
    last_answer: LastAnswer = LastAnswer()
    photo: Optional[bytes] = None
    email: Optional[str] = None
    # other extra info


class User(BaseModel):
    login: str      # id
    password: str   # hash
    settings: Settings = Settings()
    user_settings: UserSettings = UserSettings()


class TokenPayload(BaseModel):
    expires_delta: str
    login: str


class AlgorithmParams(BaseModel):
    restriction: Restriction


# copy-paste from algo-service
class InvestStrategy(BaseModel):
    profit: float = 0
    distribution: Dict[str, float] = dict()  # [0 .. 1] (= % / 100) For all CURRENT_INDEXES.
