from dotbimpy import *


def create_pyramid_mesh():
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

    return Mesh(mesh_id=0, coordinates=coordinates, indices=indices)


def create_cube_mesh():
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

    return Mesh(mesh_id=0, coordinates=coordinates, indices=faces_ids)


def create_pyramid_element():
    color = Color(r=255, g=255, b=0, a=255)
    guid = "76e051c1-1bd7-44fc-8e2e-db2b64055068"
    info = {"Name": "Pyramid"}
    rotation = Rotation(qx=0, qy=0, qz=0, qw=1.0)
    type = "Structure"
    vector = Vector(x=0, y=0, z=0)
    return Element(mesh_id=0,
                   vector=vector,
                   guid=guid,
                   info=info,
                   rotation=rotation,
                   type=type,
                   color=color)


def create_red_cube_element():
    return Element(mesh_id=0,
                   color=Color(255, 0, 0, 255),
                   vector=Vector(x=-100.0, y=-100.0, z=-100.0),
                   rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                   guid="9f61b565-06a2-4bef-8b72-f37091ab54d6",
                   info={"Name": "Red Cube"},
                   type="Brick")


def create_green_cube_element():
    return Element(mesh_id=0,
                   color=Color(0, 255, 0, 126),
                   vector=Vector(x=-0.0, y=0.0, z=0.0),
                   rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                   guid="4d00c967-791a-42a6-a5e8-cf05831bc11d",
                   info={"Name": "Green Cube"},
                   type="Brick")


def create_blue_cube_element():
    return Element(mesh_id=0,
                   color=Color(0, 0, 255, 10),
                   vector=Vector(x=100.0, y=100.0, z=100.0),
                   rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                   guid="8501a5e3-4709-47d8-bd5d-33d745a435d5",
                   info={"Name": "Blue Cube"},
                   type="Brick")


def create_file_with_pyramid():
    mesh = create_pyramid_mesh()
    element = create_pyramid_element()
    file_info = {
        "Author": "John Doe",
        "Date": "28.09.1999"
    }

    return File("1.0.0", meshes=[mesh], elements=[element], info=file_info)


def create_file_with_cubes():
    mesh = create_cube_mesh()
    red_cube = create_red_cube_element()
    green_cube = create_green_cube_element()
    blue_cube = create_blue_cube_element()
    file_info = {"Author": "John Doe"}

    file = File(schema_version="1.0.0",
                meshes=[mesh],
                elements=[red_cube, green_cube, blue_cube],
                info=file_info)
    return file
