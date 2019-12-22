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

        input1 = int(program[curr + 1])
        if opcode == 99:
            break
        elif opcode == 3:
            program[input1] = p_input.pop(0)
            curr += 2
        elif opcode == 4:
            print(input1 if p1_is_val else program[input1])
            curr += 2
        elif opcode in [1, 2]:
            val1 = input1 if p1_is_val else int(program[input1])
            input2 = int(program[curr + 2])
            val2 = input2 if p2_is_val else int(program[input2])
            res = val1 + val2 if opcode == 1 else val1 * val2
            pos = int(program[curr + 3])
            program[pos] = res
            curr += 4
        else:
            raise Exception("Unknown program code %s" % program[curr])
    print("res:", program[0])

def main():
    f = open('5_input', 'r')
    program = f.readline().split(',')
    run_program(program, [1])

main()