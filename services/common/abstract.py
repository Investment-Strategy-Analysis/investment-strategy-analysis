from pydantic import BaseModel
from typing import List, Dict, Optional, Union
from enum import Enum
import datetime
# from services.common.consts import YEAR
YEAR = 365


class AnyList(BaseModel):   # only for internal
    data: List[BaseModel]


class InvestItem(BaseModel):
    name: str = ""
    country: str = ""
    id: Optional[str] = None
    date_from: datetime.date = datetime.date(1000, 1, 1)
    date_till: datetime.date = datetime.date(1000, 1, 1)
    history: List[float] = []


class CheckboxInfo(BaseModel):
    id: str
    name: str


class AnalysisTimeInfo(BaseModel):
    id: str
    name: str
    days: int


class Checkbox(Enum):
    ONLY_RUSSIAN = CheckboxInfo(name="Only Russian assets", id="ONLY_RUSSIAN")
    WITHOUT_ASSETS = CheckboxInfo(name="Without assets", id="WITHOUT_ASSETS")
    WITHOUT_BONDS = CheckboxInfo(name="Without bonds", id="WITHOUT_BONDS")
    WITHOUT_GOLD = CheckboxInfo(name="Without gold", id="WITHOUT_GOLD")
    HIGH_DIVERSIFICATION = CheckboxInfo(name="High diversification", id="HIGH_DIVERSIFICATION")


class AnalysisTime(Enum):
    DAY_1 = AnalysisTimeInfo(name="1 day", id="DAY_1", days=1)
    DAY_100 = AnalysisTimeInfo(name="100 days", id="DAY_100", days=100)
    YEAR_1 = AnalysisTimeInfo(name="1 year", id="YEAR_1", days=YEAR)
    YEAR_3 = AnalysisTimeInfo(name="3 years", id="YEAR_3", days=YEAR * 3)
    YEAR_5 = AnalysisTimeInfo(name="5 years", id="YEAR_5", days=YEAR * 5)
    YEAR_10 = AnalysisTimeInfo(name="10 years", id="YEAR_10", days=YEAR * 10)
    # add ...


class Index(Enum):
    IMOEX = InvestItem(name='Индекс МосБиржи индекс РТС (IMOEX)', country='russia', id='IMOEX')
    # RGBI = InvestItem(name='Индекс государственных облигаций РФ (RGBI)', country='russia', id='RGBI')
    MOEXBC = InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC')
    MOEXBMI = InvestItem(name='Индекс широкого рынка (MOEXBMI)', country='russia', id='MOEXBMI')
    MCXSM = InvestItem(name='Индекс средней и малой капитализации (MCXSM)', country='russia', id='MCXSM')
    # SPX = InvestItem(name='Индекс американских акций S&P 500 (SPX)', country='foreign', id='SPX')
    # GDAXI = InvestItem(name='Индекс немецких акций DAX (GDAXI)', country='foreign', id='GDAXI')
    # IXIC = InvestItem(name='Индекс американских IT акций NASDAQ Composite (IXIC)', country='foreign', id='IXIC')
    # CIH = InvestItem(name='Акции китайских компаний (CIH)', country='foreign', id='CIH')


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
    analysis_time: Union[str, int] = AnalysisTime.YEAR_1.value.id
