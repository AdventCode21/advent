import os.path
import time
from collections import defaultdict


def sign(num):
    return 1 if num >= 0 else -1


def process(data, diagonal):
    vents = defaultdict(int)
    for line in data:
        points = line.split(" -> ")
        x1 = int(points[0].split(",")[0])
        y1 = int(points[0].split(",")[1])
        x2 = int(points[1].split(",")[0])
        y2 = int(points[1].split(",")[1])
        if x1 == x2:
            extra = sign(y2 - y1)
            for i in range(y1, y2 + extra, extra):
                vents[(x1, i)] += 1
        elif y1 == y2:
            extra = sign(x2 - x1)
            for i in range(x1, x2 + extra, extra):
                vents[(i, y1)] += 1
        elif diagonal:
            if abs(x1 - x2) == abs(y1 - y2):
                extra_x = sign(x2 - x1)
                extra_y = sign(y2 - y1)
                for x, y in zip(
                    range(x1, x2 + extra_x, extra_x), range(y1, y2 + extra_y, extra_y)
                ):
                    vents[(x, y)] += 1

    return sum([1 for i in vents if vents[i] > 1])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data_d5.txt")) as f:
        data = f.read().splitlines()
        print(process(data, False))
        print(process(data, True))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
