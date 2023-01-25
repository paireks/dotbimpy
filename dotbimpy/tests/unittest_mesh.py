from dotbimpy import *
import pytest


def test_init():
    mesh = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])

    assert mesh.mesh_id == 4
    assert mesh.coordinates == [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0]
    assert mesh.indices == [0, 1, 2]


@pytest.mark.parametrize("mesh_id, coordinates, indices, expected",
                         [(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
                          (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], False),
                          (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 1, 2], False),
                          (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 2, 1], False),
                          (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 2, 1], False)])
def test_eq(mesh_id, coordinates, indices, expected):
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = Mesh(mesh_id, coordinates, indices)

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


@pytest.mark.parametrize("mesh_id, coordinates, indices, expected",
                         [(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
                          (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
                          (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 1, 2], False),
                          (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 2, 1], False),
                          (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 2, 1], False)])
def test_equals_without_mesh_id(mesh_id, coordinates, indices, expected):
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = Mesh(mesh_id, coordinates, indices)

    assert original.equals_without_mesh_id(other) == expected
    assert other.equals_without_mesh_id(original) == expected
