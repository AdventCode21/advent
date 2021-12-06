import time


def d1_p1(numbers):
    count = 0
    for i in range(len(numbers) - 1):
        old = numbers[i]
        new = numbers[i + 1]
        if old < new:
            count += 1
    return count


def d1_p2(numbers):
    count = 0
    for i in range(len(numbers) - 3):
        old = numbers[i] + numbers[i + 1] + numbers[i + 2]
        new = numbers[i + 1] + numbers[i + 2] + numbers[i + 3]
        if old < new:
            count += 1
    return count


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("data.txt") as f:
        data = f.readlines()
    numbers = [int(x.strip()) for x in data]

    print(d1_p1(numbers))
    print(d1_p2(numbers))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
