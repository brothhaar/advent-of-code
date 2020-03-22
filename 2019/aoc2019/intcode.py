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
    inputs = []
    output_value = None

    def __init__(self, inputs=None):
        if inputs is None:
            inputs = []
        self.inputs = inputs

    def op_add(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        op3 = code[ip + 3]
        code[op3] = op1 + op2
        print('%d add %d %d => %d' % (ip, op1, op2, op3))
        return ip + 4, code

    def op_mul(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        op3 = code[ip + 3]
        code[op3] = op1 * op2
        print('%d mul %d %d => %d' % (ip, op1, op2, op3))
        return ip + 4, code

    def op_input(self, ip, code, param_modes):
        op1 = code[ip + 1]
        input =  self.inputs.pop(0)
        code[op1] = input
        print('%d input %d => %d' % (ip, input, op1))
        return ip + 2, code

    def op_output(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        self.output_value = op1
        print('%d output %d => %d' % (ip, self.output_value, op1))
        print('OUTPUT %d' % self.output_value)
        return ip + 2, code

    def op_jump_if_true(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        print('%d jump_if_true %d %d' % (ip, op1, op2))
        if op1 != 0:
            return op2, code
        return ip + 3, code

    def op_jump_if_false(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        print('%d jump_if_false %d %d' % (ip, op1, op2))
        if op1 == 0:
            return op2, code
        return ip + 3, code

    def op_less_than(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        op3 = code[ip + 3]
        print('%d less_than %d %d => %d' % (ip, op1, op2, op3))
        if op1 < op2:
            code[op3] = 1
        else:
            code[op3] = 0
        return ip + 4, code

    def op_equals(self, ip, code, param_modes):
        op1 = get_operand(code, ip + 1, param_modes[0])
        op2 = get_operand(code, ip + 2, param_modes[1])
        op3 = code[ip + 3]
        print('%d equals %d %d => %d' % (ip, op1, op2, op3))
        if op1 == op2:
            code[op3] = 1
        else:
            code[op3] = 0
        return ip + 4, code

    operations = {
        1: op_add,
        2: op_mul,
        3: op_input,
        4: op_output,
        5: op_jump_if_true,
        6: op_jump_if_false,
        7: op_less_than,
        8: op_equals
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
