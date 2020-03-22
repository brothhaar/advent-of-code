from aoc2019.day08.part1 import SpaceImage, SpaceImageLayer


def test_space_image():
    si = SpaceImage("0222112222120000", 2, 2)
    assert si.merge() == ["01", "10"]

