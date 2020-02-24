from aoc2019.day01.part2 import fuel


def test_fuel():
    assert fuel(14) == 2
    assert fuel(1969) == 966
    assert fuel(100756) == 50346
