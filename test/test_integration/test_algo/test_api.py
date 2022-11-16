import requests

from test import SERVER_URL


def test_ping():
    url = f"{SERVER_URL}/ping"
    r = requests.get(url=url)
    assert r.ok
    assert r.content == b'"pong"'
