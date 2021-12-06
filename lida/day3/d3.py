import time
from collections import defaultdict


def get_digits(numbers, digit):
    ones = sum([int(n[digit]) for n in numbers])
    if ones >= len(numbers) / 2:
        most = [n for n in numbers if n[digit] == "1"]
        less = [n for n in numbers if n[digit] == "0"]
    else:
        most = [n for n in numbers if n[digit] == "0"]
        less = [n for n in numbers if n[digit] == "1"]

    return most, less


def d3_p2(data):
    digit = 0
    most = less = data
    while len(most) > 1:
        most, _ = get_digits(most, digit)
        digit += 1
    digit = 0
    while len(less) > 1:
        _, less = get_digits(less, digit)
        digit += 1

    return int(most[0], 2) * int(less[0], 2)


def d3_p1(data):
    digits = defaultdict(lambda: [0, 0])

    for line in data:
        for i in range(len(line)):
            if line[i] == "0":
                digits[i][0] += 1
            elif line[i] == "1":
                digits[i][1] += 1
    gamma = ""
    epsilon = ""
    for digit in range(len(digits)):
        if digits[digit][0] > digits[digit][1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def process(x):
    return x.strip()


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("data_d3.txt") as f:
        data = f.readlines()
    numbers = [process(x) for x in data]
    print(d3_p1(numbers))
    print(d3_p2(numbers))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
