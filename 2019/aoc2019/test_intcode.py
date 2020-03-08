from aoc2019.intcode import IntCodeComputer, parse_instruction



def test_compute():
    icc = IntCodeComputer()
    assert icc.compute([99]) == [99]
    assert icc.compute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert icc.compute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert icc.compute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert icc.compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert icc.compute([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]
    assert icc.compute([1101, 100, -1, 4, 0]) == [1101, 100, -1, 4, 99]


def test_input_output():
    icc = IntCodeComputer(42)
    assert icc.compute([3, 0, 4, 0, 99]) == [42, 0, 4, 0, 99]
    assert icc.get_output() == 42


def test_parse_instruction():
    assert parse_instruction(1002) == (2, [0, 1, 0])
    assert parse_instruction(2) == (2, [0, 0, 0])
