import sys


def main():
    f = open('1a_input', 'r')
    result = 0
    for row in f.readlines():
        result += int(row)
    print("result", result)

main()