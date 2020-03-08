import pathlib
from aoc2019.intcode import IntCodeComputer, parse_code

if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        code_str = f.readline()
        code = parse_code(code_str)
        icc = IntCodeComputer()
        ans = icc.compute(code)
        print('answer: %s' % ans[0])
