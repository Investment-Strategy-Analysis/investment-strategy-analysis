import pytest as pytest
import sys
sys.path.append('C:\\Users\\mozha\\HOMEWORK\\7sem\\PI\\investment-strategy-analysis')

test_data = [
    (2, 2, 4),
]


@pytest.mark.parametrize("a, b, c", test_data)
def test_simple(a, b, c):
    assert a + b == c


def test_exception():
    try:
        a = 2 / 0
    except:
        return
    assert 'divide by zero'