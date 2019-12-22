import sys

def run_program(program, p_input):
    curr = 0
    p_len = len(program)
    while p_len > curr:
        op_input = int(program[curr])
        dm_op = divmod(op_input, 10000)
        p3_is_val = dm_op[0]
        dm_op = divmod(dm_op[1], 1000)
        p2_is_val = dm_op[0]
        dm_op = divmod(dm_op[1], 100)
        p1_is_val = dm_op[0]
        opcode = dm_op[1]

        if opcode == 99:
            return None

        input1 = int(program[curr + 1])
        if opcode == 3:
            program[input1] = p_input.pop(0)
            curr += 2
        elif opcode == 4:
            return input1 if p1_is_val else program[input1]
        elif opcode in [1, 2, 7, 8]:
            val1 = input1 if p1_is_val else int(program[input1])
            input2 = int(program[curr + 2])
            val2 = input2 if p2_is_val else int(program[input2])

            if opcode == 1:
                res = val1 + val2
            elif opcode == 2:
                res = val1 * val2
            elif opcode == 7:
                res = 1 if val1 < val2 else 0
            elif opcode == 8:
                res = 1 if val1 == val2 else 0
            program[int(program[curr + 3])] = res
            curr += 4
        elif opcode == 5:
            val1 = input1 if p1_is_val else int(program[input1])
            if val1:
                input2 = int(program[curr + 2])
                curr = input2 if p2_is_val else int(program[input2])
            else:
                curr += 3
        elif opcode == 6:
            val1 = input1 if p1_is_val else int(program[input1])
            if val1:
                curr += 3
            else:
                input2 = int(program[curr + 2])
                curr = input2 if p2_is_val else int(program[input2])
        else:
            raise Exception("Unknown program code %s" % program[curr])
    raise Exception("No return")


def generate_permutations(num_elem_to_process, a, out):
    if num_elem_to_process == 1:
        return None

    generate_permutations(num_elem_to_process-1, a, out)

    for i in range(num_elem_to_process-1):
        if num_elem_to_process % 2 == 0:
            ai = a[i]
            a[i] = a[num_elem_to_process-1]
            a[num_elem_to_process-1] = ai
        else:
            a0 = a[0]
            a[0] = a[num_elem_to_process-1]
            a[num_elem_to_process-1] = a0
        out.append(a.copy())
        generate_permutations(num_elem_to_process-1, a, out)


def find(phase_settings, program):
    amplifiers = {}
    for phase_setting in phase_settings:
        amplifiers[phase_setting] = program.copy()
    output = 0
    for _ in range(10):
        for phase_setting in phase_settings:
            o = run_program(amplifiers[phase_setting], [phase_setting, output])
            if o is None:
                return output
            output = o
            print('ps', phase_setting)
            print('o', output)
    return output

def main():
    f = open('test', 'r')
    program = f.readline().split(',')
    ps_combinations = []
    init = [9, 8, 7, 6, 5]
    generate_permutations(5, init, ps_combinations)
    ps_combinations.append(init)

    print('go')
    print('res', find(init, program))

    result = 0
    for phase_settings in ps_combinations:
        output = find(phase_settings, program)
        result = result if output <= result else output
    print('Result: ', result)
main()