import copy
import os.path
import time
from collections import defaultdict


def calculate(rules, polymer, days):
    for _ in range(days):
        new_rules = copy.deepcopy(rules)
        for i in rules:
            c = rules[i][0]
            n = rules[i][1]
            if n:
                new_rules[f"{i[0]}{c}"][1] += n
                new_rules[f"{c}{i[1]}"][1] += n
                new_rules[i][1] -= n
        rules = copy.deepcopy(new_rules)
    count = defaultdict(int)
    for i in rules:
        count[i[0]] += rules[i][1] / 2
        count[i[1]] += rules[i][1] / 2
    count[polymer[0]] += 0.5
    count[polymer[-1]] += 0.5
    sort = sorted(count.values())
    return int(sort[-1] - sort[0])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        rules = {}
        polymer = f.readline().strip()
        f.readline()
        while True:
            line = f.readline().strip()
            if not line:
                break
            rule = line.split(" -> ")
            rules[rule[0]] = [rule[1], 0]
        for i in range(len(polymer) - 1):
            comb = f"{polymer[i]}{polymer[i+1]}"
            rules[comb][1] += 1

        print(calculate(rules, polymer, 10))
        print(calculate(rules, polymer, 40))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
