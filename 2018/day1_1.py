import sys


def main():
    f = open('day1_1_input.txt', 'r')
    result = 0
    for row in f.readlines():
        result += int(row)
    print("result", result)

main()