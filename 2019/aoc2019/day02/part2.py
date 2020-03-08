import pathlib
from aoc2019.intcode import IntCodeComputer, parse_code


def find_inputs(code_str, exp):
    for noun in range(0, 100):
        for verb in range(0, 100):
            code = parse_code(code_str)
            code[1] = noun
            code[2] = verb
            icc = IntCodeComputer()
            ans = icc.compute(code)
            if ans[0] == exp:
                return 100 * noun + verb


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        code_str = f.readline()
        ans = find_inputs(code_str, 19690720)
        print('answer: %d' % ans)
