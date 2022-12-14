import requests
import pytest

from test.test_integration.test_algo.consts import SERVER_URL


# @pytest.fixture(autouse=True)
# def wait_server():
#     assert True
#
#     url = f"{SERVER_URL}/ping"
#     stop = False
#
#     while not stop:
#         try:
#             r = requests.get(url=url)
#             if r.ok:
#                 stop = True
#         except Exception:
#             pass
#
#     yield
#     assert True


def test_ping():
    url = f"{SERVER_URL}/ping"
    r = requests.get(url=url)
    assert r.ok
    assert r.content == b'"pong"'
