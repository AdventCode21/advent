import os.path
import time

from collections import deque


chars = {"{": "}", "<": ">", "(": ")", "[": "]"}
points = {"}": 1197, ">": 25137, ")": 3, "]": 57}
scores = {")": 1, "]": 2, "}": 3, ">": 4}


def part1(data):
    count = 0
    for line in data:
        queue = deque([])
        for char in line:
            if char in chars:
                queue.appendleft(chars[char])
            else:
                check = queue.popleft()
                if char != check:
                    count += points[char]
                    break
    return count


def part2(data):
    incomplete = []
    for line in data:
        corrupted = False

        queue = deque([])
        for char in line:
            if char in chars:
                queue.appendleft(chars[char])
            else:
                check = queue.popleft()
                if char != check:
                    corrupted = True
                    break
        if queue and not corrupted:
            score = 0
            for char in queue:
                score = 5 * score + scores[char]
            incomplete.append(score)
    middle = int(len(incomplete) / 2)
    return sorted(incomplete)[middle]


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()
        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
