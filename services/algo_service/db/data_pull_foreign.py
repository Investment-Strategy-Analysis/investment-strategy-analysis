import requests
from requests.adapters import HTTPAdapter
import json
import datetime
import logging
from services.algo_service.common.consts import LINKS_PULL_FOREIGN_DATA, DATE_PULL, MAX_DAYS
from services.algo_service.common.singletons import CURRENT_INDEXES
from services.algo_service.db.data_db_api import save_history, load_history


def get_data_or_empty(link):
    to_day = datetime.date.today().strftime(DATE_PULL)
    from_day = (datetime.date.today() - datetime.timedelta(days=MAX_DAYS * 6.9 / 5)).strftime(DATE_PULL)
    result = requests.get(link.format(from_day, to_day))
    if result.status_code == 200:
        print(result.text)
        data_dict = json.loads(result.text)
        if 'data' in data_dict:
            return [float(i['last_max'].replace(',', '')) / 2 + float(i['last_min'].replace(',', '')) / 2
                    for i in data_dict['data']]
        else:
            logging.error(f'Failed to parse, no data: {link.format(from_day, to_day)}. '
                          'Error code = {result.status_code}')
            return []
    else:
        logging.error(f'Failed request: {link.format(from_day, to_day)}. Error code = {result.status_code}')
        return []


def get_and_set_usd():
    CURRENT_INDEXES['USD'].history = get_data_or_empty(LINKS_PULL_FOREIGN_DATA["USD"])


def get_history_in_rub(id="GOLD"):
    usd_data = get_data_or_empty(LINKS_PULL_FOREIGN_DATA[id])
    for i in range(len(usd_data)):
        usd_data[-i] *= CURRENT_INDEXES["USD"].history[-i]
    return usd_data


def renew_foreign_data_if_necessary():
    logging.info(f'Pulling Foreign Data.')
    print(f'Pulling Foreign Data.')
    if False and not CURRENT_INDEXES['USD'].history:
        for index in CURRENT_INDEXES.values():
            load_history(index)
    logging.info(f'Index = {CURRENT_INDEXES}')
    get_and_set_usd()
    for (_, index) in CURRENT_INDEXES.items():
        if index.country == 'foreign' and index.id != "USD":
            index.history = get_history_in_rub(index.id)
    logging.info(f'Foreign data pulling completed.')
    for (_, index) in CURRENT_INDEXES.items():
        save_history(index)
    logging.info(f'Index = {CURRENT_INDEXES}')

