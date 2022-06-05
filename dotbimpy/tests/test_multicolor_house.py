from dotbimpy import *


def test_multicolor_house___view():
    bim_file = File.read("MulticolorHouse.bim")
    bim_file.view()


def test_multicolor_house___view_with_face_colors():
    bim_file = File.read("MulticolorHouse.bim")
    bim_file.view_with_face_colors()
