from services.algo_service.common.abstract import InvestItem
import datetime

CURRENT_INDEXES = {
    'IMOEX': InvestItem(name='Индекс МосБиржи индекс РТС (IMOEX)', country='russia', id='IMOEX'),
    'RGBI': InvestItem(name='Индекс государственных облигаций РФ (RGBI)', country='russia', id='RGBI'),
    'MOEXBC': InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC'),
    'MOEXBMI': InvestItem(name='Индекс широкого рынка (MOEXBMI)', country='russia', id='MOEXBMI'),
    'RUCBITR': InvestItem(name='Индекс Мосбиржи корп обл CBITR (RUCBITR)', country='russia', id='RUCBITR'),
    'MCXSM': InvestItem(name='Индекс средней и малой капитализации (MCXSM)', country='russia', id='MCXSM'),
    # InvestItem(name='Индекс американских акций S&P 500 (SPX)', country='foreign', id='SPX'),
    # InvestItem(name='Индекс немецких акций DAX (GDAXI)', country='foreign', id='GDAXI'),
    # InvestItem(name='Индекс американских IT акций NASDAQ Composite (IXIC)', country='foreign', id='IXIC'),
    # InvestItem(name='Акции китайских компаний (CIH)', country='foreign', id='CIH')
}

LAST_RENEW_TIME = datetime.datetime(year=2000, month=1, day=2, minute=1, second=1, microsecond=1)