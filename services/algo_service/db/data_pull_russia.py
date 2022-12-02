import random
import requests
from requests.adapters import HTTPAdapter
import logging
import json
import xmltodict
import datetime
from services.algo_service.common.consts import LINK_PULL_DATA, LINK_PULL_DATES, DATE_PULL
from services.algo_service.common.singletons import CURRENT_INDEXES
#from services.algo_service.db.data_db_api import save_history, load_history


def pull_data(date='2010-10-23'):
    s = requests.Session()
    s.mount('http://stackoverflow.com', HTTPAdapter(max_retries=5))
    result = requests.get(f'{LINK_PULL_DATA}{date}')
    if result.status_code == 200:
        data_dict = json.loads(result.text)
        if 'history' in data_dict:
            if 'data' in data_dict['history']:
                return {i[1].upper(): i[5] for i in data_dict['history']['data'] if i[1].upper() in CURRENT_INDEXES.keys()}
            else:
                logging.error(f'Failed to parse, no data: {LINK_PULL_DATA}{date}. Error code = {result.status_code}')
                return None
        else:
            logging.error(f'Failed to parse, no history: {LINK_PULL_DATA}{date}. Error code = {result.status_code}')
            return None
    else:
        logging.error(f'Failed request: {LINK_PULL_DATA}{date}. Error code = {result.status_code}')
        return None


def pull_date():
    result = requests.get(LINK_PULL_DATES)
    if result.status_code == 200:
        return {i['@indexid']: [datetime.datetime.strptime(i['@from'], "%Y-%m-%d").date(),
                                datetime.datetime.strptime(i['@till'], "%Y-%m-%d").date()]
                for i in xmltodict.parse(result.text)['document']['data']['rows']['row']}
    else:
        logging.error(f'Failed request: {LINK_PULL_DATES}. Error code = {result.status_code}')
        return None


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(days=n)


def renew_russian_data_if_necessary():
    logging.info(f'Pulling Russian Data.')
    #if False and not CURRENT_INDEXES['IMOEX'].history:
    #    for index in CURRENT_INDEXES.values():
    #        load_history(index)
    dates = pull_date()
    needs_new_data = []
    min_date = None
    max_date = None
    for (_, index) in CURRENT_INDEXES.items():
        if index.country == 'russia':
            if max_date is None or max_date < index.date_till:
                max_date = index.date_till
            if max_date < dates[index.id][1]:
                max_date = dates[index.id][1]
    for (_, index) in CURRENT_INDEXES.items():
        if index.country == 'russia':
            if index.date_till < dates[index.id][1]:
                needs_new_data.append(index.id)
                if index.date_till == index.date_from:
                    index.date_from = index.date_till = dates[index.id][0]
                    if min_date is None or min_date > index.date_from:
                        min_date = index.date_from
                else:
                    if min_date is None or min_date > index.date_till + datetime.timedelta(days=1):
                        min_date = index.date_till + datetime.timedelta(days=1)
    min_date = datetime.date(year=2021, month=8, day=4)
    max_date = datetime.date(year=2021, month=9, day=4)
    for date in daterange(min_date, max_date):
        if date.weekday() <= 4:
            data = pull_data(date.strftime(DATE_PULL))
            for (index_id, price) in data.items():
                index = CURRENT_INDEXES[index_id]
                if index.date_till.weekday() == 4:
                    index.date_till += datetime.timedelta(days=2)
                if index.date_till < date:
                    index.history.append(price)
                    index.date_till += datetime.timedelta(days=1)
            for (index_id, index) in CURRENT_INDEXES.items():  # prolongs some data that wasn't updated recently.
                if index.country == 'russia':
                    if index.date_till.weekday() == 4:  # Needs to be re updated later TODO
                        index.date_till += datetime.timedelta(days=2)
                    if index.date_till < date:
                        index.date_till += datetime.timedelta(days=1)
                        if len(index.history) > 0:
                            index.history.append(index.history[-1])
                        else:
                            logging.warning(f'Failed call [-1] of history of {index_id} {date}.')
                            index.date_from = index.date_till = date
            if random.randint(0, 90) == 0:
                logging.info(f'Current date {date}. End date {max_date}')
                #for index_id in data.keys():
                #    save_history(CURRENT_INDEXES[index_id])
    logging.info(f'Russian data pulling completed.')
    #for (_, index) in CURRENT_INDEXES.items():
    #    save_history(index)
    logging.info(f'Index = {CURRENT_INDEXES}')