from aoc2019.day04.part1 import check_password


def test_check_password():
    assert check_password(111111) is True
    assert check_password(111123) is True
    assert check_password(223450) is False
    assert check_password(123789) is False
