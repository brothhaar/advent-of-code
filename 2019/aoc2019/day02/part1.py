import pathlib
from aoc2019.intcode import parse, compute

if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        code_str = f.readline()
        code = parse(code_str)
        ans = compute(code)
        print('answer: %s' % ans[0])
