import os.path
import time

from collections import defaultdict


def find_neighbors(x, y, rows, cols):
    return [
        (x0, y0)
        for x0 in range(x - 1, x + 2)
        for y0 in range(y - 1, y + 2)
        if (
            (x != x0 or y != y0)
            and (0 <= x0 < rows)
            and (0 <= y0 < cols)
            and abs(x0 - x + y0 - y) == 1
        )
    ]


def find_min(x, y, data):
    neighbors = [
        data[i[0]][i[1]] for i in find_neighbors(x, y, len(data), len(data[0]))
    ]
    return data[x][y] < min(neighbors)


def find_basins(minimum, data):
    basin = set()
    visited = set()
    queue = [minimum]
    while queue:
        point = queue.pop()
        if not point in visited:
            visited.add(point)
            if data[point[0]][point[1]] < 9:
                basin.add(point)
                queue.extend(
                    find_neighbors(point[0], point[1], len(data), len(data[0]))
                )
    return basin


def part1(data):

    mins = []
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if find_min(i, j, data):
                mins.append((i, j))
                count += data[i][j] + 1

    return mins, count


def part2(data, mins):
    basins = []
    for i in mins:
        basin = find_basins(i, data)
        if basin not in basins:
            basins.append(basin)

    sizes = sorted([len(basin) for basin in basins], reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [[int(char) for char in line] for line in f.read().splitlines()]
        mins, count = part1(data)
        print("sum of the risk levels of all low points:", count)
        print("product sizes of the three largest basins:", part2(data, mins))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
