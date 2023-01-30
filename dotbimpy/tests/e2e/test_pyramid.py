from ..test_helper import *


def test_pyramid():
    file = create_file_with_pyramid()
    file.save("Pyramid.bim")

    read_file = File.read("Pyramid.bim")

    assert read_file.schema_version == "1.0.0"
    assert read_file.info == file.info

    assert len(read_file.elements) == 1
    read_element = read_file.elements[0]
    assert read_element.type == file.elements[0].type
    assert read_element.info == file.elements[0].info
    assert read_element.mesh_id == file.elements[0].mesh_id
    assert read_element.rotation == file.elements[0].rotation
    assert read_element.vector == file.elements[0].vector
    assert read_element.color == file.elements[0].color
    assert read_element.guid == file.elements[0].guid

    read_mesh = read_file.meshes[0]
    assert read_mesh.mesh_id == file.meshes[0].mesh_id
    assert read_mesh.coordinates == file.meshes[0].coordinates
    assert read_mesh.indices == file.meshes[0].indices

    assert read_file == file
