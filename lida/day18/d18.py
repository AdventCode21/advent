import json
import itertools
import math
import os.path
import time


def magnitude(element):
    if type(element) is list:
        return 3 * magnitude(element[0]) + 2 * magnitude(element[1])
    elif type(element) is int:
        return element
    return


def splitNumber(element, split=False):
    if split:
        return element, True
    if isinstance(element, int):
        if element > 9:
            half = element / 2
            return [int(half), int(math.ceil(half))], True
        return element, False
    else:
        element[0], split = splitNumber(element[0], split)
        element[1], split = splitNumber(element[1], split)
        return element, split


def addLeft(pair, number):
    if isinstance(pair, int):
        return pair + number
    return [addLeft(pair[0], number), pair[1]]


def addRight(pair, number):
    if isinstance(pair, int):
        return pair + number
    return [pair[0], addRight(pair[1], number)]


def explode(element, depth=0):
    if isinstance(element, int):
        return element, False, 0, 0
    if depth == 4:
        return 0, True, element[0], element[1]
    left, exploded, sumLeft, sumRight = explode(element[0], depth + 1)
    if exploded:
        return [left, addLeft(element[1], sumRight)], True, sumLeft, 0
    right, exploded, sumLeft, sumRight = explode(element[1], depth + 1)
    if exploded:
        return [addRight(element[0], sumLeft), right], True, 0, sumRight
    return [left, right], False, 0, 0


def reduce(L):
    explodeCheck = True
    while explodeCheck:
        L, explodeCheck, _, _ = explode(L)
    L, splitCheck = splitNumber(L)
    if splitCheck:
        return reduce(L)
    return L


def part1(data):
    start = data.pop(0)
    while data:
        start = reduce([start, data.pop(0)])
    return magnitude(start)


def part2(data):
    magnitudes = []
    couples = list(itertools.combinations(data, 2))
    for couple in couples:
        magnitudes.append(magnitude(reduce([couple[0], couple[1]])))
        magnitudes.append(magnitude(reduce([couple[1], couple[0]])))
    return max(magnitudes)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [json.loads(line) for line in f.read().splitlines()]
        magn = part1(data.copy())
        print(f"part1: {magn}")
        maxmagn = part2(data)
        print(f"part2: {maxmagn}")

    # Keep this line at the end of your code

    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
