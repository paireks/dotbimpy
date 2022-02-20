from dotbimpy import *


def test_pyramid():
    coordinates = [
        # Base
        0.0, 0.0, 0.0,
        10.0, 0.0, 0.0,
        10.0, 10.0, 0.0,
        0.0, 10.0, 0.0,

        # Top
        5.0, 5.0, 4.0
    ]

    indices = [
        # Base faces
        0, 1, 2,
        0, 2, 3,

        # Side faces
        0, 1, 4,
        1, 2, 4,
        2, 3, 4,
        3, 0, 4
    ]

    mesh = Mesh(mesh_id=0, coordinates=coordinates, indices=indices)
    color = Color(r=255, g=255, b=0, a=255)
    guid = "76e051c1-1bd7-44fc-8e2e-db2b64055068"
    info = {"Name": "Pyramid"}
    rotation = Rotation(qx=0, qy=0, qz=0, qw=1.0)
    type = "Structure"
    vector = Vector(x=0, y=0, z=0)
    element = Element(mesh_id=0,
                      vector=vector,
                      guid=guid,
                      info=info,
                      rotation=rotation,
                      type=type,
                      color=color)

    file_info = {
        "Author": "John Doe",
        "Date": "28.09.1999"
    }

    file = File("1.0.0", meshes=[mesh], elements=[element], info=file_info)
    file.save("Pyramid.bim")

    read_file = File.read("Pyramid.bim")

    assert read_file.schema_version == "1.0.0"
    assert read_file.info == file_info

    assert len(read_file.elements) == 1
    read_element = read_file.elements[0]
    assert read_element.type == element.type
    assert read_element.info == element.info
    assert read_element.mesh_id == element.mesh_id
    assert read_element.rotation == element.rotation
    assert read_element.vector == element.vector
    assert read_element.color == element.color
    assert read_element.guid == element.guid

    read_mesh = read_file.meshes[0]
    assert read_mesh.mesh_id == mesh.mesh_id
    assert read_mesh.coordinates == mesh.coordinates
    assert read_mesh.indices == mesh.indices

    assert read_file == file
