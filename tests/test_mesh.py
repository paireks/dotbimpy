from dotbimpy import Mesh
import pytest
from pydantic import ValidationError


def test_init():
    mesh = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])

    assert mesh.mesh_id == 4
    assert mesh.coordinates == [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0]
    assert mesh.indices == [0, 1, 2]


@pytest.mark.parametrize(
    "mesh_id, coordinates, indices, expected",
    [
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
        (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], False),
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 1, 2], False),
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 2, 1], False),
        (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 2, 1], False),
    ],
)
def test_eq(mesh_id, coordinates, indices, expected):
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = Mesh(mesh_id, coordinates, indices)

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


def test_eq_with_other_object():
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = 2

    assert original.__eq__(other) is False


@pytest.mark.parametrize(
    "mesh_id, coordinates, indices, expected",
    [
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
        (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2], True),
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 1, 2], False),
        (4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 2, 1], False),
        (3, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.1, 0.0, 20.0], [0, 2, 1], False),
    ],
)
def test_equals_without_mesh_id(mesh_id, coordinates, indices, expected):
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = Mesh(mesh_id, coordinates, indices)

    assert original.equals_without_mesh_id(other) == expected
    assert other.equals_without_mesh_id(original) == expected


def test_equals_without_mesh_id_with_other_object():
    original = Mesh(4, [0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 20.0], [0, 1, 2])
    other = 2

    assert original.equals_without_mesh_id(other) is False


class TestMeshValidation:
    def test_empty_mesh(self):
        m = Mesh()
        assert m.coordinates == []
        assert m.indices == []

    def test_one_vertex_no_faces(self):
        m = Mesh(mesh_id=0, coordinates=[1.0, 2.0, 3.0], indices=[])
        assert len(m.coordinates) == 3
        assert len(m.indices) == 0

    def test_valid_single_triangle(self):
        m = Mesh(
            mesh_id=0,
            coordinates=[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            indices=[0, 1, 2],
        )
        assert len(m.coordinates) == 9
        assert len(m.indices) == 3

    def test_coordinates_not_divisible_by_3(self):
        with pytest.raises(
            ValidationError, match="len\\(coordinates\\) must be divisible by 3"
        ):
            Mesh(mesh_id=0, coordinates=[1.0, 2.0], indices=[0])

    def test_indices_not_divisible_by_3(self):
        with pytest.raises(
            ValidationError, match="len\\(indices\\) must be divisible by 3"
        ):
            Mesh(mesh_id=0, coordinates=[1.0, 2.0, 3.0], indices=[0])

    def test_index_out_of_range(self):
        with pytest.raises(
            ValidationError, match="Index 2 out of range for 1 vertices"
        ):
            Mesh(mesh_id=0, coordinates=[1.0, 2.0, 3.0], indices=[0, 1, 2])

    def test_indices_with_empty_coordinates(self):
        with pytest.raises(
            ValidationError,
            match="Indices reference vertices but coordinates list is empty",
        ):
            Mesh(mesh_id=0, coordinates=[], indices=[0, 1, 2])
