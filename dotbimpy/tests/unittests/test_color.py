from dotbimpy import *
import pytest


def test_init():
    color = Color(31, 30, 50, 4)

    assert color.r == 31
    assert color.g == 30
    assert color.b == 50
    assert color.a == 4


@pytest.mark.parametrize("r, g, b, a, expected",
                         [(31, 30, 50, 4, True),
                          (32, 30, 50, 4, False),
                          (31, 29, 50, 4, False),
                          (31, 30, 51, 4, False),
                          (31, 30, 50, 5, False),
                          (32, 29, 51, 5, False)])
def test_eq(r, g, b, a, expected):
    original = Color(31, 30, 50, 4)
    other = Color(r, g, b, a)

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


def test_eq_with_other_object():
    original = Color(31, 30, 50, 4)
    other = 2

    assert original.__eq__(other) is NotImplemented
