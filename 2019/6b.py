import sys


class Planet:
    def __init__(self, name):
        self.name = name
        self.children = []


def num_children_orbits(parent, num_parents):
    res = num_parents
    for child in parent.children:
        res += num_children_orbits(child, num_parents + 1)
    return res


def main():
    f = open('6_input', 'r')

    planets = dict()
    for line in f.readlines():
        orbit = line.split(')')
        p_name = orbit[0]
        c_name = orbit[1].rstrip()
        if p_name not in planets:
            planets[p_name] = Planet(p_name)
        if c_name not in planets:
            planets[c_name] = Planet(c_name)
        planets[c_name].parent = planets[p_name]
        planets[p_name].children.append(planets[c_name])

    current = planets["YOU"].parent
    parents = dict()
    count = 0
    while current.name != 'COM':
        parents[current.name] = count
        current = current.parent
        count += 1

    current = planets["SAN"].parent
    count = 0
    while 1:
        if current.name in parents:
            print("Res ", count + parents[current.name])
            break
        count += 1
        current = current.parent


main()