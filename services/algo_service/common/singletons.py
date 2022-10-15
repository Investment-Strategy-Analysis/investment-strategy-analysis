from services.algo_service.common.abstract import InvestItem
import datetime

CURRENT_INDEXES = {
    'RTSI': InvestItem(name='Индекс РТС (RTSI)', country='russia', id='RTSI'),
    'RTSOG': InvestItem(name='Индекс РТС нефти и газа (RTSOG)', country='russia', id='RTSOG'),
    # 'RGBI': InvestItem(name='RGBI Индекс государственных облигаций РФ (MCXRGBI)', country='russia', id='RGBI'),
    # 'MOEXBC': InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC'),
    # 'RUCBITR': InvestItem(name='Индекс Мосбиржи корпоративных облигаций (RUCBITR)', country='russia', id='RUCBITR'),
    # InvestItem(name='Индекс американских акций S&P 500 (SPX)', country='foreign', id='SPX'),
    # InvestItem(name='Индекс немецких акций DAX (GDAXI)', country='foreign', id='GDAXI'),
    # InvestItem(name='Индекс американских IT акций NASDAQ Composite (IXIC)', country='foreign', id='IXIC'),
    # InvestItem(name='Акции китайских компаний (CIH)', country='foreign', id='CIH')
}

LAST_RENEW_TIME = datetime.datetime(year=2000, month=1, day=2, minute=1, second=1, microsecond=1)
