import aiohttp

DATEFMT = "%Y-%m-%dT%H:%M:%S"
JWT_DATEFMT = "%Y-%m-%d %H:%M:%S.%f"
OK = "ok"

# jwt
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"

# post
ALGORITHM_SERVICE_HOST = "http://algo-service:8080"
AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=1 * 60 * 60)      # hour
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}
