from ..test_helper import *


def test_init_pyramid():

    file = create_file_with_pyramid()

    assert file.schema_version == "1.0.0"
    assert file.info == {
        "Author": "John Doe",
        "Date": "28.09.1999"
    }

    assert len(file.elements) == 1
    assert file.elements[0].type == "Structure"
    assert file.elements[0].info == {"Name": "Pyramid"}
    assert file.elements[0].mesh_id == 0
    assert file.elements[0].rotation == Rotation(qx=0, qy=0, qz=0, qw=1.0)
    assert file.elements[0].vector == Vector(x=0, y=0, z=0)
    assert file.elements[0].color == Color(r=255, g=255, b=0, a=255)
    assert file.elements[0].guid == "76e051c1-1bd7-44fc-8e2e-db2b64055068"

    assert len(file.meshes) == 1
    assert file.meshes[0].mesh_id == 0
    assert file.meshes[0].coordinates == [
        # Base
        0.0, 0.0, 0.0,
        10.0, 0.0, 0.0,
        10.0, 10.0, 0.0,
        0.0, 10.0, 0.0,

        # Top
        5.0, 5.0, 4.0
    ]
    assert file.meshes[0].indices == [
        # Base faces
        0, 1, 2,
        0, 2, 3,

        # Side faces
        0, 1, 4,
        1, 2, 4,
        2, 3, 4,
        3, 0, 4
    ]


def test_init_cubes():

    file = create_file_with_cubes()

    assert file.schema_version == "1.0.0"
    assert file.info == {"Author": "John Doe"}

    red_cube = Element(mesh_id=0,
                       color=Color(255, 0, 0, 255),
                       vector=Vector(x=-100.0, y=-100.0, z=-100.0),
                       rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                       guid="9f61b565-06a2-4bef-8b72-f37091ab54d6",
                       info={"Name": "Red Cube"},
                       type="Brick")

    green_cube = Element(mesh_id=0,
                         color=Color(0, 255, 0, 126),
                         vector=Vector(x=-0.0, y=0.0, z=0.0),
                         rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                         guid="4d00c967-791a-42a6-a5e8-cf05831bc11d",
                         info={"Name": "Green Cube"},
                         type="Brick")

    blue_cube = Element(mesh_id=0,
                        color=Color(0, 0, 255, 10),
                        vector=Vector(x=100.0, y=100.0, z=100.0),
                        rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                        guid="8501a5e3-4709-47d8-bd5d-33d745a435d5",
                        info={"Name": "Blue Cube"},
                        type="Brick")

    assert len(file.elements) == 3
    assert file.elements[0] == red_cube
    assert file.elements[1] == green_cube
    assert file.elements[2] == blue_cube

    assert len(file.meshes) == 1
    assert file.meshes[0].mesh_id == 0
    assert file.meshes[0].coordinates == [
        0.0, 0.0, 0.0,
        10.0, 0.0, 0.0,
        10.0, 0.0, 20.0,
        0.0, 0.0, 20.0,
        0.0, 30.0, 0.0,
        10.0, 30.0, 0.0,
        10.0, 30.0, 20.0,
        0.0, 30.0, 20.0
    ]
    assert file.meshes[0].indices == [
        # Front side
        0, 1, 2,
        0, 2, 3,

        # Bottom side
        0, 1, 4,
        1, 4, 5,

        # Left side
        0, 4, 3,
        4, 3, 7,

        # Right side
        1, 2, 5,
        2, 5, 6,

        # Top side
        2, 3, 7,
        2, 6, 7,

        # Back side
        4, 5, 7,
        5, 6, 7
    ]

