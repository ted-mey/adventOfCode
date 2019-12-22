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
            break

        input1 = int(program[curr + 1])
        if opcode == 3:
            program[input1] = p_input.pop(0)
            curr += 2
        elif opcode == 4:
            print(input1 if p1_is_val else program[input1])
            curr += 2
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
    print("res:", program[0])

def main():
    f = open('5_input', 'r')
    program = f.readline().split(',')
    run_program(program, [5])
main()