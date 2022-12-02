from services.common.consts import *


LINK_PULL_DATA = 'https://iss.moex.com/iss/history/engines/stock/markets/index/securities.json?date='
LINK_PULL_DATES = 'https://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics'
DATE_PULL = "%Y-%m-%d"
DATEFMT = "%Y-%m-%dT%H:%M:%S"


LINKS_PULL_FOREIGN_DATA = {
    "GOLD": "http://api.scraperlink.com/investpy/?email=lesnik-a-a@yandex.ru&type=historical_data&product=commodities"
            "&from_date={}&to_date={}&time_frame=Daily&name=gold",
    "SPX": "http://api.scraperlink.com/investpy/?email=lesnik-a-a@yandex.ru&type=historical_data&product=indices"
           "&from_date={}&to_date={}&time_frame=Daily&symbol=SPX",
    "GDAXI": "http://api.scraperlink.com/investpy/?email=lesnik-a-a@yandex.ru&type=historical_data&product=indices"
           "&from_date={}&to_date={}&time_frame=Daily&symbol=GDAXI",
    "IXIC": "http://api.scraperlink.com/investpy/?email=lesnik-a-a@yandex.ru&type=historical_data&product=indices"
           "&from_date={}&to_date={}&time_frame=Daily&symbol=IXIC",
    "USD": "http://api.scraperlink.com/investpy/?email=lesnik-a-a@yandex.ru&type=historical_data&product"
           "=currency_crosses&name=USD/RUB&from_date={}&to_date={}"
}