import sys


def main():
    f = open('2a_input', 'r')
    program = f.readline().split(',')

    #Reset to "1202 program alarm"
    program[1] = 12
    program[2] = 2

    curr = 0
    p_len = len(program)
    while p_len > curr:
        if int(program[curr]) == 99:
            print('Found end (99)')
            break

        val1 = int(program[int(program[curr+1])])
        val2 = int(program[int(program[curr+2])])
        if int(program[curr]) == 1:
            res = val1 + val2
        elif int(program[curr]) == 2:
            res = val1 * val2
        else:
            raise Exception("Unknown program code %s" % program[curr])
        pos = int(program[curr+3])
        program[pos] = res
        print('pos',pos)
        print('res',res)
        print(program)
        curr += 4
    print(program)
    print('Result on index 0: %s' % program[0])

main()