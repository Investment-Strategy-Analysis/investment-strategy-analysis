import requests
import pytest

from test.test_integration.test_user.consts import SERVER_URL


@pytest.fixture(autouse=True)
def wait_server():
    assert True

    url = f"{SERVER_URL}/ping"
    stop = False

    while not stop:
        try:
            r = requests.get(url=url)
            if r.ok:
                stop = True
        except Exception:
            pass

    yield
    assert True


def test_ping():
    url = f"{SERVER_URL}/ping"
    r = requests.get(url=url)
    assert r.ok
    assert r.content == b'"pong"'


def test_checkboxes():
    url = f"{SERVER_URL}/settings/checkboxes"
    r = requests.get(url=url)

    assert r.ok
    content = r.json()

    assert len(content['data']) == 5
    assert content['data'][0]['id'] == "ONLY_RUSSIAN"


def test_strategies():
    url = f"{SERVER_URL}/settings/strategies"
    r = requests.get(url=url)

    assert r.ok
    content = r.json()

    assert len(content['data']) == 5
    assert content['data'][0]['id'] == "strategy_1"
    assert content['data'][0]['profit'] == 25
    assert content['data'][0]['risk'] == 10
