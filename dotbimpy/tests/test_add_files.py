from dotbimpy import *
import copy


def test__add__pyramid_cubes():
    file_a = File.read("Pyramid.bim")
    file_b = File.read("Cubes.bim")

    file_result = file_a + file_b

    assert file_result.schema_version == file_a.schema_version
    assert file_result.info == file_a.info

    # Check meshes
    assert file_result.meshes[0] == file_a.meshes[0]
    assert file_result.meshes[1].equals_without_mesh_id(file_b.meshes[0])
    assert file_result.meshes[1].mesh_id == 1

    # Check elements
    assert file_result.elements[0] == file_a.elements[0]
    assert file_result.elements[1].equals_without_mesh_id(file_b.elements[0]) and file_result.elements[1].mesh_id == 1
    assert file_result.elements[2].equals_without_mesh_id(file_b.elements[1]) and file_result.elements[2].mesh_id == 1
    assert file_result.elements[3].equals_without_mesh_id(file_b.elements[2]) and file_result.elements[3].mesh_id == 1


def test__add__cubes_pyramid():
    file_a = File.read("Cubes.bim")
    file_b = File.read("Pyramid.bim")

    file_result = file_a + file_b

    assert file_result.schema_version == file_a.schema_version
    assert file_result.info == file_a.info
    assert file_result.meshes[1].mesh_id == 1

    # Check meshes
    assert file_result.meshes[0] == file_a.meshes[0]
    assert file_result.meshes[1].equals_without_mesh_id(file_b.meshes[0])

    # Check elements
    assert file_result.elements[0] == file_a.elements[0]
    assert file_result.elements[1] == file_a.elements[1]
    assert file_result.elements[2] == file_a.elements[2]
    assert file_result.elements[3].equals_without_mesh_id(file_b.elements[0]) and file_result.elements[3].mesh_id == 1


def test__add__walls_truss__check_if_originals_changed():
    file_a = File.read("WallsWithBeams.bim")
    file_b = File.read("Truss.bim")
    file_a_copy = copy.deepcopy(file_a)
    file_b_copy = copy.deepcopy(file_b)

    file_result = file_a + file_b

    assert file_a == file_a_copy
    assert file_b == file_b_copy


def test__add__walls_truss():
    file_a = File.read("WallsWithBeams.bim")
    file_b = File.read("Truss.bim")

    file_result = file_a + file_b

    assert file_result.schema_version == file_a.schema_version
    assert file_result.info == file_a.info

    # Check meshes
    assert file_result.meshes[0] == file_a.meshes[0]
    assert file_result.meshes[1] == file_a.meshes[1]
    for i in range(5):
        assert file_result.meshes[i+2].equals_without_mesh_id(file_b.meshes[i])

    # Check elements
    for i in range(7):
        assert file_result.elements[i] == file_a.elements[i]

    for i in range(7, len(file_result.elements)):
        assert file_result.elements[i].equals_without_mesh_id(file_b.elements[i-7])

