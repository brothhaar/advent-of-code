from operator import add, mul

opcodes = {
    1: add,
    2: mul,
}


def parse(code_str):
    code = []
    for op in code_str.split(','):
        code.append(int(op))
    return code


def unparse(code):
    return ','.join(map(str, code))


def compute(code):
    i = 0
    while code[i] != 99:
        op = code[i]
        op1_pos = code[i + 1]
        op2_pos = code[i + 2]
        out_pos = code[i + 3]
        opcode = opcodes.get(op)
        code[out_pos] = opcode.__call__(code[op1_pos], code[op2_pos])
        i = i + 4
    return code


with open('input') as f:
    code_str = f.readline()
    code = parse(code_str)
    ans = compute(code)
    print('answer: %s' % unparse(ans))
