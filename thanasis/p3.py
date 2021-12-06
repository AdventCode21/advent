import sys
import copy

def parse_input():
    oxygen, co2 = [], []
    with open(sys.argv[1]) as file:
        oxygen = file.readlines()
        co2 = copy.copy(oxygen)
    return oxygen, co2

def findMostCommonDigit(n):
    ones, zeros = 0, 0
    for i in n:
        if i == '0':
            zeros += 1
        else:
            ones += 1
    return str(int(ones >= zeros))

def updateList(rating, idx, digit, flag):
    idxs = []
    for i, rate in enumerate(rating):
        if flag:
            if rate[idx] != digit:
                idxs.append(i)
        else:
            if rate[idx] == digit:
                idxs.append(i)
    for i in idxs[::-1]:
        rating.pop(i)

def ex2(oxygen, co2):
    idx_ox, idx_co2 = 0, 0
    while len(oxygen) > 1 or len(co2) > 1:
        if len(oxygen) > 1:
            updateList(oxygen, idx_ox, findMostCommonDigit(list(zip(*oxygen))[idx_ox]), True)
            idx_ox += 1
        if len(co2) > 1:
            updateList(co2, idx_co2, findMostCommonDigit(list(zip(*co2))[idx_co2]), False)
            idx_co2 += 1
    return int(oxygen[0], 2) * int(co2[0], 2)

if __name__ == "__main__":
    oxygen, co2 = parse_input()
    print(ex2(oxygen, co2))