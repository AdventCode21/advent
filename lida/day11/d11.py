import os.path
import time

flashes = 0


def find_neighbors(x, y, rows, cols):
    return [
        (x0, y0)
        for x0 in range(x - 1, x + 2)
        for y0 in range(y - 1, y + 2)
        if ((x != x0 or y != y0) and (0 <= x0 < rows) and (0 <= y0 < cols))
    ]


def find_tens(data, flashed):
    return {
        (ix, iy)
        for ix, row in enumerate(data)
        for iy, i in enumerate(row)
        if i > 9 and (ix, iy) not in flashed
    }


def flashing(data):
    data = [[i + 1 for i in line] for line in data]
    flashes = 0
    flashed = set()
    tens = find_tens(data, flashed)
    while tens:
        flash = tens.pop()
        flashed.add(flash)
        flashes += 1
        neighbors = find_neighbors(flash[0], flash[1], len(data), len(data[0]))
        for i in neighbors:
            data[i[0]][i[1]] += 1
        tens = find_tens(data, flashed)
    data = [[i if i < 10 else 0 for i in line] for line in data]

    return data, flashes


def part1(data, days):

    count = 0
    for _ in range(days):
        data, flashes = flashing(data)
        count += flashes

    return count


def part2(data):

    day = 0
    flash = 0
    total = len(data) * len(data[0])
    while flash != total:
        day += 1
        data, flash = flashing(data)

    return day


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [[int(char) for char in line] for line in f.read().splitlines()]
        print(part1(data, 100))
        print(part2(data))
        # print("product sizes of the three largest basins:", part2(data, mins))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
