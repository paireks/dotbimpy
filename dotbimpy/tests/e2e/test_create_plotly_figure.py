from dotbimpy import *


def test_create_plotly_figure___multiple_meshes___check_json():

    bim_file = File.read("MultipleMeshes.bim")
    figure = bim_file.create_plotly_figure()
    actual = str(figure.to_json())

    with open(r"text_file/plotly_multiple_meshes.txt") as f:
        expected = f.read()

    bim_file.view()

    assert actual == expected

