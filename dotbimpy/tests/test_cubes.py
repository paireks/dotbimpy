from dotbimpy import *


def test_cubes():
    coordinates = [
        0.0, 0.0, 0.0,
        10.0, 0.0, 0.0,
        10.0, 0.0, 20.0,
        0.0, 0.0, 20.0,
        0.0, 30.0, 0.0,
        10.0, 30.0, 0.0,
        10.0, 30.0, 20.0,
        0.0, 30.0, 20.0
    ]

    faces_ids = [
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

    mesh = Mesh(mesh_id=0, coordinates=coordinates, indices=faces_ids)

    red_cube = Element(mesh_id=0,
                       color=Color(255, 0, 0, 255),
                       vector=Vector(x=-100.0, y=-100.0, z=-100.0),
                       rotation=Rotation(qx=0.1, qy=0.3, qz=0.4, qw=1.0),
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
                        rotation=Rotation(qx=-2.2, qy=-1.4, qz=1.5, qw=-1.2),
                        guid="8501a5e3-4709-47d8-bd5d-33d745a435d5",
                        info={"Name": "Blue Cube"},
                        type="Brick")

    file_info = {"Author": "John Doe"}

    file = File(schema_version="1.0.0",
                meshes=[mesh],
                elements=[red_cube, green_cube, blue_cube],
                info=file_info)

    file.save("Cubes.bim")

    read_file = file.read("Cubes.bim")

    assert read_file == file
