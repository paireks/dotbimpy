from dotbimpy import *
import pytest


def test_init():
    rotation = Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500)

    assert rotation.qx == 0.6397929577145492
    assert rotation.qy == 0.1062698214791025
    assert rotation.qz == -0.1247209304773680
    assert rotation.qw == -0.750877077691500


@pytest.mark.parametrize("qx, qy, qz, qw, expected",
                         [(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500, True),
                          (0.6397929578145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500, False),
                          (0.6397929577145492, -0.1062698214791025, -0.1247209304773680, -0.750877077691500, False),
                          (0.6397929577145492, 0.1062698214791025, -0.1447209304773680, -0.750877077691500, False),
                          (0.5397929577145492, 0.1162698214791025, -0.1447209304773680, -0.750877077691500, False)])
def test_eq(qx, qy, qz, qw, expected):
    original = Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500)
    other = Rotation(qx, qy, qz, qw)

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


def test_eq_with_other_object():
    original = Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500)
    other = 2

    assert original.__eq__(other) is NotImplemented
