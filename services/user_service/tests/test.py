import pytest


@pytest.mark.parametrize(
    "a, b, c",
    [
        (2, 2, 4),
        (1, 2, 3),
    ]
)
def test_simple(a, b, c):
    assert a + b == c
