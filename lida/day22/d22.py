import itertools
import math
import os.path
import re
import time

from collections import defaultdict, Counter


def execute1(steps):
    cubes = set()

    for step in steps:
        a = [step[1], step[2], step[3]]
        coordinates = set(itertools.product(*a))
        if step[0]:
            cubes = cubes.union(coordinates)
        else:
            cubes = cubes.difference(coordinates)

    return len(cubes)


def ex(steps):
    cubes = defaultdict(int)

    for step in steps:
        a = [step[1], step[2], step[3]]
        coordinates = list(itertools.product(*a))
        for c in coordinates:
            if cubes[c] != step[0]:
                cubes[c] = step[0]

    return Counter(cubes.values())[1]


def overlap(cube1, cube2):
    if any([c2[0] > c1[1] or c2[1] < c1[0] for c1, c2 in zip(cube1, cube2)]):
        return None
    else:
        return tuple(
            [(max(c1[0], c2[0]), min(c1[1], c2[1])) for c1, c2 in zip(cube1, cube2)]
        )


def getvolume(cube):
    return math.prod([c[1] + 1 - c[0] for c in cube])


def ex2(steps):
    cubes = defaultdict(int)
    for step in steps:
        new = tuple([step[1], step[2], step[3]])
        new_cubes = cubes.copy()
        for cube in cubes:
            overlaping = overlap(cube, new)
            if overlaping:
                new_cubes[overlaping] -= new_cubes[cube]
        cubes = new_cubes.copy()
        if step[0]:
            cubes[new] += 1
    volume = 0
    for cube in cubes:
        volume += cubes[cube] * getvolume(cube)

    return volume


def check_coordinates(cmin, cmax):
    checker = set(range(-50, 51))
    checking = set(range(cmin, cmax + 1))
    return checking.intersection(checker)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()
        steps1 = []
        steps2 = []
        for d in data:
            on = 1 if d.split()[0] == "on" else 0
            coordinates = [int(digit) for digit in re.findall(r"[-]?\d+", d)]
            x1 = check_coordinates(coordinates[0], coordinates[1])
            y1 = check_coordinates(coordinates[2], coordinates[3])
            z1 = check_coordinates(coordinates[4], coordinates[5])
            if x1 and y1 and z1:
                steps1.append((on, list(x1), list(y1), list(z1)))
            steps2.append(
                (
                    on,
                    (coordinates[0], coordinates[1]),
                    (coordinates[2], coordinates[3]),
                    (coordinates[4], coordinates[5]),
                )
            )

        print(ex(steps1))
        print(ex2(steps2))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
