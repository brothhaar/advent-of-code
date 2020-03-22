from aoc2019.intcode import IntCodeComputer, parse_code
import pathlib
import itertools


class Amplifier:
    def __init__(self, code):
        self.code = code.copy()
        self.computer = IntCodeComputer()

    def single_mode(self, inputs):
        self.computer.set_inputs(inputs)
        self.code = self.computer.compute(self.code)
        return self.get_output()

    def feedback_mode(self, inputs):
        self.computer.set_inputs(inputs)
        self.code = self.computer.compute_until_output(self.code)
        return self.get_output()

    def get_output(self):
        return self.computer.get_output()

    def is_done(self):
        return self.computer.done


def max_thruster(code, phase_settings):
    (a, b, c, d, e) = phase_settings
    print("checking", a, b, c, d, e)
    amp_a = Amplifier(code)
    amp_b = Amplifier(code)
    amp_c = Amplifier(code)
    amp_d = Amplifier(code)
    amp_e = Amplifier(code)

    out_a = amp_a.single_mode([a, 0])
    out_b = amp_b.single_mode([b, out_a])
    out_c = amp_c.single_mode([c, out_b])
    out_d = amp_d.single_mode([d, out_c])
    out_e = amp_e.single_mode([e, out_d])

    return out_e


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        code_str = f.readline()
        code = parse_code(code_str)
        permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
        max_output = 0
        for ps in permutations:
            out = max_thruster(code, ps)
            if out > max_output:
                max_output = out
        print('answer: %d' % max_output)
