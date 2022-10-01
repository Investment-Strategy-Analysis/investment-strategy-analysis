import aiohttp
from services.user_service.common.consts import AIOHTTP_TIMEOUT, HEADERS


async def post(path: str, data: str):
    async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
        async with session.post(path, data=data, headers=HEADERS) as response:
            return await response.json()
