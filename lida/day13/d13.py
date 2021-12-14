import os.path
import time
from collections import defaultdict


def part1(rows, cols, instruction):
    points = 0
    if instruction[0] == "x":
        n = instruction[1]
        d = cols.copy()
    else:
        n = instruction[1]
        d = rows.copy()
    for i in list(d.keys()):
        if i > n:
            diff = i - n
            d[n - diff].update(d[i])
            d.pop(i)
    points = sum([len(d[i]) for i in d])

    return points


def part2(rows, cols, instructions):

    for instruction in instructions:
        if instruction[0] == "x":
            a = cols
            b = rows
        else:
            a = rows
            b = cols
        n = instruction[1]
        for i in list(a.keys()):
            if i > n:
                diff = i - n
                a[n - diff].update(a[i])
                for j in a[i]:
                    b[j].add(n - diff)
                    b[j].remove(i)
                a.pop(i)

    M = max(rows.keys())
    N = max(cols.keys())
    array = [["."] * (N + 1) for _ in range(M + 1)]
    for row in rows:
        for i in rows[row]:
            array[row][i] = "#"

    for row in array:
        print(" ".join(row))

    return


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:

        # first section
        rows = defaultdict(set)
        cols = defaultdict(set)
        while True:
            line = f.readline().strip()
            if not line:
                break
            point = line.split(",")
            cols[int(point[0])].add(int(point[1]))
            rows[int(point[1])].add(int(point[0]))

        # second section
        instructions = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            inst = line.split("=")
            instructions.append((inst[0][-1], int(inst[1])))

        print(part1(rows, cols, instructions[0]))
        part2(rows, cols, instructions)

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
