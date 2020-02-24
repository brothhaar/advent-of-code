from aoc2019.day01.part1 import fuel


def test_fuel():
    assert fuel(12) == 2
    assert fuel(14) == 2
    assert fuel(1969) == 654
    assert fuel(100756) == 33583
