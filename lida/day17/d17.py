import os.path
import re
import time


def part1(y_min):
    return int(y_min * (y_min + 1) / 2)


def part2(data):
    x1, x2, y1, y2 = data[0], data[1], data[2], data[3]
    count = 0
    for y in range(y1, abs(y1)):
        for x in range(1, x2 + 1):
            vx, vy = x, y
            x_p = y_p = 0
            for t in range(2 * abs(y1) + 2):
                x_p += vx
                y_p += vy
                vx = max(vx - 1, 0)
                vy -= 1
                if x1 <= x_p <= x2 and y1 <= y_p <= y2:
                    count += 1
                    break
                elif x_p > x2 or y_p < y1:
                    break
    return count


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [int(i) for i in re.findall(r"[-]?\d+", f.read())]
        print(part1(data[2]))
        print(part2(data))
    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
