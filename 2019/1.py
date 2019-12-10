import sys

def calc_fuel(mass):
    return int((mass/3)-2)

def main():
    f = open('1_input', 'r')

    fuel_rec = 0
    for mass in f.readlines():
        fuel_rec += calc_fuel(int(mass))
    print("Total fuel requirements: ", fuel_rec)

main()