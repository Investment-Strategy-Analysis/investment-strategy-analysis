import aiohttp
from services.common.consts import DATEFMT


JWT_DATEFMT = "%Y-%m-%d %H:%M:%S.%f"
OK = "ok"

# jwt
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"

# post
ALGORITHM_SERVICE_HOST = "http://algo-service:8000"
AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=1 * 60 * 60)      # hour
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}
