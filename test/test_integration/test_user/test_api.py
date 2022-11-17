import requests

from test.test_integration.test_user.consts import SERVER_URL


def test_ping():
    url = f"{SERVER_URL}/ping"
    r = requests.get(url=url)
    assert r.ok
    assert r.content == b'"pong"'
