from aoc2019.day04.part2 import check_password


def test_check_password():
    assert check_password(112233) is True
    assert check_password(123444) is False
    assert check_password(111122) is True
