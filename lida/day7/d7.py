import os.path
import time
from collections import defaultdict

import numpy as np


def part1(data):
    fuel = []
    for point in range(min(data), max(data) + 1):
        fuel.append(sum([abs(i - point) for i in data]))

    return min(fuel)


def part2(data):
    fuel = []
    for point in range(min(data), max(data) + 1):
        fuel.append(sum([abs(i - point) * (abs(i - point) + 1) / 2 for i in data]))

    return min(fuel)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [int(i) for i in f.read().splitlines()[0].split(",")]

    print(part1(data))
    print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
