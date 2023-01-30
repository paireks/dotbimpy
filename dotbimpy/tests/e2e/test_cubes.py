from ..test_helper import *


def test_cubes():

    file = create_file_with_cubes()
    file.save("Cubes.bim")
    read_file = File.read("Cubes.bim")

    assert read_file == file


def test_view():

    file = create_file_with_cubes()
    file.view()
