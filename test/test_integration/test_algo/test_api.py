import requests

from test.test_integration.test_algo.consts import SERVER_URL


def test_ping():
    url = f"https://ya.ru"
    r = requests.get(url=url)
    assert r.ok
    assert r.content == b'"pong"'
