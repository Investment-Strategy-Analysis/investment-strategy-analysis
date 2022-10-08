from services.algo_service.common.abstract import InvestItem

CURRENT_INDEXES = {
    'RTSI': InvestItem(name='Индекс РТС (RTSI)', country='russia', id='RTSI'),
    #'RGBI': InvestItem(name='RGBI Индекс государственных облигаций РФ (MCXRGBI)', country='russia', id='RGBI'),
    'MOEXBC': InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC'),
    #'RUCBITR': InvestItem(name='Индекс Мосбиржи корпоративных облигаций (RUCBITR)', country='russia', id='RUCBITR'),
    # InvestItem(name='Индекс американских акций S&P 500 (SPX)', country='foreign', id='SPX'),
    # InvestItem(name='Индекс немецких акций DAX (GDAXI)', country='foreign', id='GDAXI'),
    # InvestItem(name='Индекс американских IT акций NASDAQ Composite (IXIC)', country='foreign', id='IXIC'),
    # InvestItem(name='Акции китайских компаний (CIH)', country='foreign', id='CIH')
}
