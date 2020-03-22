from aoc2019.intcode import IntCodeComputer, parse_code
from aoc2019.day07.part1 import Amplifier
import pathlib
import itertools


def feedback_loop(code, phase_settings):
    (a, b, c, d, e) = phase_settings
    print("checking", a, b, c, d, e)
    amp_a = Amplifier(code)
    amp_b = Amplifier(code)
    amp_c = Amplifier(code)
    amp_d = Amplifier(code)
    amp_e = Amplifier(code)

    out_a = amp_a.feedback_mode([a, 0])
    out_b = amp_b.feedback_mode([b, out_a])
    out_c = amp_c.feedback_mode([c, out_b])
    out_d = amp_d.feedback_mode([d, out_c])
    out_e = amp_e.feedback_mode([e, out_d])

    while not amp_e.is_done():
        out_a = amp_a.feedback_mode([out_e])
        out_b = amp_b.feedback_mode([out_a])
        out_c = amp_c.feedback_mode([out_b])
        out_d = amp_d.feedback_mode([out_c])
        out_e = amp_e.feedback_mode([out_d])

    return out_e


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        code_str = f.readline()
        code = parse_code(code_str)
        permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
        max_output = 0
        for ps in permutations:
            out = feedback_loop(code, ps)
            if out > max_output:
                max_output = out
        print('answer: %d' % max_output)
