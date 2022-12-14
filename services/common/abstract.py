from pydantic import BaseModel
from typing import List, Dict, Optional
from enum import Enum
import datetime
# from services.common.consts import YEAR
from services.common.consts import MAX_DAYS
YEAR = 365


class AnyList(BaseModel):   # only for internal
    data: List[BaseModel]


class InvestItem(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    id: str
    date_from: datetime.date = datetime.date(1000, 1, 1)
    date_till: datetime.date = datetime.date(1000, 1, 1)
    history: List[float] = []


class CheckboxInfo(BaseModel):
    id: str
    name: str


class Checkbox(Enum):
    ONLY_RUSSIAN = CheckboxInfo(name="Only Russian assets", id="ONLY_RUSSIAN")
    WITHOUT_ASSETS = CheckboxInfo(name="Without assets", id="WITHOUT_ASSETS")
    WITHOUT_BONDS = CheckboxInfo(name="Without bonds", id="WITHOUT_BONDS")
    WITHOUT_GOLD = CheckboxInfo(name="Without gold", id="WITHOUT_GOLD")
    HIGH_DIVERSIFICATION = CheckboxInfo(name="High diversification", id="HIGH_DIVERSIFICATION")


class Index(Enum):
    RUB = InvestItem(name='Рубль (RUB/RUR)', country='const', id='RUB', history=([1] * MAX_DAYS))
    IMOEX = InvestItem(name='Индекс МосБиржи индекс РТС (IMOEX)', country='russia', id='IMOEX')
    #MOEXBC = InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC')
    #MOEXBMI = InvestItem(name='Индекс широкого рынка (MOEXBMI)', country='russia', id='MOEXBMI')
    MCXSM = InvestItem(name='Индекс средней и малой капитализации (MCXSM)', country='russia', id='MCXSM')
    SPX = InvestItem(name='Индекс американских акций S&P 500 (SPX)', country='foreign', id='SPX')
    GDAXI = InvestItem(name='Индекс немецких акций DAX (GDAXI)', country='foreign', id='GDAXI')
    IXIC = InvestItem(name='Индекс американских IT акций NASDAQ Composite (IXIC)', country='foreign', id='IXIC')
    GOLD = InvestItem(name='Золото', country='foreign', id='GOLD')
    USD = InvestItem(name='Доллар США (USD)', country='foreign', id='USD')


class InvestStrategy(BaseModel):
    id: str
    description: Optional[str] = None
    profit: float = 0
    risk: float = 0
    distribution: Dict[str, float] = {Index.IMOEX.name : 1}   # key - Index.name, [0 .. 1] (= % / 100) For all CURRENT_INDEXES


class Restriction(BaseModel):
    target_profit: float = 0    # used to find best point in pareto front
    checkboxes: Dict[str, bool] = {checkbox.value.id: False for checkbox in Checkbox}   # key - Checkbox.name
    upper_border: Optional[Dict[str, float]] = None     # key - Index.name
    lower_border: Optional[Dict[str, float]] = None     # key - Index.name
    analysis_time: int = YEAR
