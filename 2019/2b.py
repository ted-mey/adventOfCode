import sys

def run_program(program, input1, input2):
    program[1] = input1
    program[2] = input2

    curr = 0
    p_len = len(program)
    while p_len > curr:
        if int(program[curr]) == 99:
            break

        val1 = int(program[int(program[curr + 1])])
        val2 = int(program[int(program[curr + 2])])
        if int(program[curr]) == 1:
            res = val1 + val2
        elif int(program[curr]) == 2:
            res = val1 * val2
        else:
            raise Exception("Unknown program code %s" % program[curr])
        pos = int(program[curr + 3])
        program[pos] = res
        curr += 4
    return program[0]


def main():
    f = open('2a_input', 'r')
    program = f.readline().split(',')
    result = 0
    for noun in range(100):
        for verb in range(100):
            p_res = run_program(program.copy(), noun, verb)
            if p_res == 19690720:
                result = noun * 100 + verb

    print('Answer is %s' % result)
main()