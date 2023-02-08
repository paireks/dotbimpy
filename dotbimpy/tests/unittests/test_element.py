from dotbimpy import *
import pytest


def test_init():
    element = Element(mesh_id=0,
                      color=Color(31, 30, 50, 4),
                      guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                      vector=Vector(5, 3, 2),
                      rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                        -0.750877077691500),
                      type="Beam",
                      info={"Name": "Pyramid"})

    assert element.type == "Beam"
    assert element.info == {"Name": "Pyramid"}
    assert element.mesh_id == 0
    assert element.rotation == Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500)
    assert element.vector == Vector(5, 3, 2)
    assert element.color == Color(31, 30, 50, 4)
    assert element.guid == "8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb"


def test_init_with_face_colors():
    element = Element(mesh_id=0,
                      color=Color(31, 30, 50, 4),
                      face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                      guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                      vector=Vector(5, 3, 2),
                      rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                        -0.750877077691500),
                      type="Beam",
                      info={"Name": "Pyramid"})

    assert element.type == "Beam"
    assert element.info == {"Name": "Pyramid"}
    assert element.mesh_id == 0
    assert element.rotation == Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680, -0.750877077691500)
    assert element.vector == Vector(5, 3, 2)
    assert element.color == Color(31, 30, 50, 4)
    assert element.face_colors == [255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255]
    assert element.guid == "8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb"


@pytest.mark.parametrize("other, expected",
                         [(Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), True),
                          (Element(mesh_id=4,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 51, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="b38c62c9-4bd5-4dea-a408-0bcbd902cb0f",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(1, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0, 0, 0, 1.0),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Column",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Another Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Another name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid", "Another name": "Another Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 251],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          ])
def test_eq(other, expected):
    original = Element(mesh_id=0,
                       color=Color(31, 30, 50, 4),
                       face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                       guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                       vector=Vector(5, 3, 2),
                       rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                         -0.750877077691500),
                       type="Beam",
                       info={"Name": "Pyramid"})

    assert original.__eq__(other) == expected
    assert other.__eq__(original) == expected


def test_eq_with_other_object():
    original = Element(mesh_id=0,
                       color=Color(31, 30, 50, 4),
                       guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                       vector=Vector(5, 3, 2),
                       rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                         -0.750877077691500),
                       type="Beam",
                       info={"Name": "Pyramid"})
    other = 2

    assert original.__eq__(other) is NotImplemented


@pytest.mark.parametrize("other, expected",
                         [(Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), True),
                          (Element(mesh_id=4,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), True),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 51, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="b38c62c9-4bd5-4dea-a408-0bcbd902cb0f",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(1, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0, 0, 0, 1.0),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Column",
                                   info={"Name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Another Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Another name": "Pyramid"}), False),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid", "Another name": "Another Pyramid"}), False),
                          ])
def test_equals_without_mesh_id(other, expected):
    original = Element(mesh_id=0,
                       color=Color(31, 30, 50, 4),
                       guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                       vector=Vector(5, 3, 2),
                       rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                         -0.750877077691500),
                       type="Beam",
                       info={"Name": "Pyramid"})

    assert original.equals_without_mesh_id(other) == expected
    assert other.equals_without_mesh_id(original) == expected


def test_equals_without_mesh_id_with_other_object():
    original = Element(mesh_id=0,
                       color=Color(31, 30, 50, 4),
                       guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                       vector=Vector(5, 3, 2),
                       rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                         -0.750877077691500),
                       type="Beam",
                       info={"Name": "Pyramid"})
    other = 2

    assert original.equals_without_mesh_id(other) is NotImplemented


@pytest.mark.parametrize("element, expected",
                         [(Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   face_colors=[255, 0, 0, 255, 135, 206, 235, 255, 255, 255, 255, 255],
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), True),
                          (Element(mesh_id=0,
                                   color=Color(31, 30, 50, 4),
                                   guid="8f6bc6d0-4f24-4bd0-917a-82ab1c22a5bb",
                                   vector=Vector(5, 3, 2),
                                   rotation=Rotation(0.6397929577145492, 0.1062698214791025, -0.1247209304773680,
                                                     -0.750877077691500),
                                   type="Beam",
                                   info={"Name": "Pyramid"}), False),
                         ])
def test_check_if_has_face_colors(element, expected):
    assert element.check_if_has_face_colors() == expected
