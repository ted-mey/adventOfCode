import sys
import itertools


def main():
    f = open("1b_input")
    results = [0]
    curr = 0
    for row in itertools.cycle(f.readlines()):
        curr += int(row)
        if(curr in results):
            print("Result", curr)
            break
        else:
            results.append(curr)

main()