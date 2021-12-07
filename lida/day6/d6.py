import os.path
import time
from collections import defaultdict

import numpy as np


def generate(data, days):
    daystobirth = defaultdict(int)
    for i in data:
        daystobirth[i] += 1
    for _ in range(days):
        daystobirth = {i - 1: daystobirth[i] for i in range(9)}

        newborns = daystobirth[-1]
        daystobirth[8] = newborns
        daystobirth[6] += newborns

    daystobirth[-1] = 0
    return sum(daystobirth.values())


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data_d6.txt")) as f:
        data = [int(i) for i in f.read().splitlines()[0].split(",")]

    print(generate(data, 80))
    print(generate(data, 256))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
