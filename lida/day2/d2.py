import time


def d2_p2(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for i in instructions:
        if i[0] == "forward":
            horizontal += i[1]
            depth += aim * i[1]
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "up":
            aim -= i[1]

    return horizontal * depth


def d2_p1(instructions):
    horizontal = 0
    depth = 0

    for i in instructions:
        if i[0] == "forward":
            horizontal += i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "up":
            depth -= i[1]
    return horizontal * depth


def process(x):
    y = x.split()
    return (y[0], int(y[1]))


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("data_d2.txt") as f:
        data = f.readlines()
    instructions = [process(x) for x in data]

    print(d2_p1(instructions))
    print(d2_p2(instructions))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
