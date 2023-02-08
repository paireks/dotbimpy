from dotbimpy import *
import pytest


def test_init():
    vector = Vector(9.9266016462536, 3.3910972817343, 52.239445879618)

    assert vector.x == 9.9266016462536
    assert vector.y == 3.3910972817343
    assert vector.z == 52.239445879618


@pytest.mark.parametrize("x, y, z, expected",
                         [(9.9266016462536, 3.3910972817343, 52.239445879618, True),
                          (9.0266016462536, 3.3910972817343, 52.239445879618, False),
                          (9.9266016462536, 3.4910972817343, 52.239445879618, False),
                          (9.9266016462536, 3.3910972817343, 52.539445879618, False),
                          (9.9266016462536, 3.3810972817343, 52.539445879618, False)])
def test_eq(x, y, z, expected):
    original = Vector(9.9266016462536, 3.3910972817343, 52.239445879618)
    other = Vector(x, y, z)

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


def test_eq_with_other_object():
    original = Vector(9.9266016462536, 3.3910972817343, 52.239445879618)
    other = 2

    assert original.__eq__(other) is NotImplemented
