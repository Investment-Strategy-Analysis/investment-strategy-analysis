import os
import aiohttp
from services.common.consts import DATEFMT


JWT_DATEFMT = "%Y-%m-%d %H:%M:%S.%f"
OK = "ok"
ADMIN = os.environ["ADMIN_LOGIN"]

# jwt
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"

# post
ALGORITHM_SERVICE_HOST = "http://algo-service:8000"
ELASTICSEARCH_HOST = "http://elasticsearch:9200"
AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=1 * 60 * 60)      # hour
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}
RESTRICTION_INDEX = "restriction"
