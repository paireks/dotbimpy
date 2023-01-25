from dotbimpy import *


def test_view():

    file = File.read("BricksRotated.bim")
    file.view()
