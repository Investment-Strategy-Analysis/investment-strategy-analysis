import datetime
from services.common.singletons import *
from services.algo_service.common.abstract import Index
import copy


CURRENT_INDEXES = {index.name: copy.deepcopy(index.value) for index in Index}
LAST_RENEW_TIME = datetime.datetime(year=2000, month=1, day=2, minute=1, second=1, microsecond=1)
