from server.common.abstract import InvestItem

CURRENT_INDEXES = [
    InvestItem(name='Индекс РТС (IRTS)', country='russia', id='IRTS'),
    InvestItem(name='RGBI Индекс государственных облигаций РФ (MCXRGBI)', country='russia', id='MCXRGBI'),
    InvestItem(name='Индекс Мосбиржи голубые фишки (MOEXBC)', country='russia', id='MOEXBC'),
    InvestItem(name='Индекс Мосбиржи корпоративных облигаций (RUCBITR)', country='russia', id='RUCBITR')
]
DATEFMT = "%Y-%m-%dT%H:%M:%S"
