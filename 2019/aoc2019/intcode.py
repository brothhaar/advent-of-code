def parse_instruction(inst):
    opcode = inst % 100
    pms = int(inst / 100)
    pm0 = int(pms / 1) % 10
    pm1 = int(pms / 10) % 10
    pm2 = int(pms / 100) % 10
    param_modes = [pm0, pm1, pm2]
    return opcode, param_modes


def get_operand(code, ip, param_mode):
    if param_mode == 0:  # position
        op_pos = code[ip]
        return code[op_pos]
    if param_mode == 1:  # immediate
        return code[ip]


def parse_code(code_str):
    code = []
    for op in code_str.split(','):
        code.append(int(op))
    return code


class IntCodeComputer:
    input_value = None
    output_value = None

    def __init__(self, input_value=None):
        self.input_value = input_value

    def op_add(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        out_pos = code[ip + 3]
        code[out_pos] = op1 + op2
        return ip + 4, code

    def op_mul(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        out_pos = code[ip + 3]
        code[out_pos] = op1 * op2
        return ip + 4, code

    def op_input(self, ip, code, param_modes):
        out_pos = code[ip + 1]
        code[out_pos] = self.input_value
        return ip + 2, code

    def op_output(self, ip, code, param_modes):
        in_pos = code[ip + 1]
        self.output_value = code[in_pos]
        print('OUTPUT %d' % self.output_value)
        return ip + 2, code

    operations = {
        1: op_add,
        2: op_mul,
        3: op_input,
        4: op_output
    }

    def compute(self, code):
        ip = 0
        while code[ip] != 99:
            inst = code[ip]
            opcode, param_modes = parse_instruction(inst)
            operation = self.operations.get(opcode)
            ip, code = operation.__call__(self, ip, code, param_modes)
        return code

    def get_output(self):
        return self.output_value
