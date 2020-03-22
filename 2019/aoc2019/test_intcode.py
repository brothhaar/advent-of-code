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
    icc = IntCodeComputer([42])
    assert icc.compute([3, 0, 4, 0, 99]) == [42, 0, 4, 0, 99]
    assert icc.get_output() == 42


def test_equal_to_8():
    code_pos = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    icc = IntCodeComputer([8])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 1
    icc = IntCodeComputer([7])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 0

    code_imm = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    icc = IntCodeComputer([8])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 1
    icc = IntCodeComputer([7])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 0


def test_less_than_8():
    code_pos = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    icc = IntCodeComputer([7])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 1
    icc = IntCodeComputer([9])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 0

    code_imm = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    icc = IntCodeComputer([7])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 1
    icc = IntCodeComputer([9])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 0


def test_jump():
    code_pos = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    icc = IntCodeComputer([0])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 0
    icc = IntCodeComputer([9])
    icc.compute(code_pos.copy())
    assert icc.get_output() == 1

    code_imm = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    icc = IntCodeComputer([0])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 0
    icc = IntCodeComputer([9])
    icc.compute(code_imm.copy())
    assert icc.get_output() == 1


def test_larger():
    code = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    icc = IntCodeComputer([7])
    icc.compute(code.copy())
    assert icc.get_output() == 999
    icc = IntCodeComputer([8])
    icc.compute(code.copy())
    assert icc.get_output() == 1000
    icc = IntCodeComputer([9])
    icc.compute(code.copy())
    assert icc.get_output() == 1001


def test_parse_instruction():
    assert parse_instruction(1002) == (2, [0, 1, 0])
    assert parse_instruction(2) == (2, [0, 0, 0])
