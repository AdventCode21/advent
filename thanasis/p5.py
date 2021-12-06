import sys
import numpy as np
import collections

def generate_map(simple=True):
    m = collections.defaultdict(lambda : 0)
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            line = line.split('->')
            line = [[int(j) for j in i.strip().split(',')] for i in line]
            if line[0][0] == line[1][0]:
                max_value = max(line[0][1], line[1][1])
                min_value = min(line[0][1], line[1][1])
                for i in range(min_value, max_value + 1):
                    m[f'{line[0][0]},{i}'] += 1
            elif line[0][1] == line[1][1]:
                max_value = max(line[0][0], line[1][0])
                min_value = min(line[0][0], line[1][0])
                for i in range(min_value, max_value + 1):
                    m[f'{i},{line[0][1]}'] += 1
            else:
                if simple:
                    continue
                if line[0][0] < line[1][0]:
                    min_x = line[0][0]
                    max_x = line[1][0]
                    y1 = line[0][1]
                    y2 = line[1][1]
                else:
                    min_x = line[1][0]
                    max_x = line[0][0]
                    y1 = line[1][1]
                    y2 = line[0][1]
                slope = np.sign(y2 - y1)
                for i in range(min_x, max_x+1):
                    m[f'{i},{y1}'] += 1
                    y1 += slope
    return m

def ex1():
    m = generate_map(simple=True)
    return len([k for k, v in m.items() if v > 1])

def ex2():
    m = generate_map(simple=False)
    return len([k for k, v in m.items() if v > 1])

if __name__ == "__main__":
    print(ex1())
    print(ex2())