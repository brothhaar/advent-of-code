from aoc2019.day08.part1 import SpaceImage, SpaceImageLayer


def test_space_image():
    si = SpaceImage("123456789012", 3, 2)
    assert len(si.layers) == 2
    assert si.layers[0].data[0] == ["1", "2", "3"]
    assert si.layers[0].data[1] == ["4", "5", "6"]
    assert si.layers[1].data[0] == ["7", "8", "9"]
    assert si.layers[1].data[1] == ["0", "1", "2"]

