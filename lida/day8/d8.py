import os.path
import time

unique = [2, 3, 4, 7]


def part1(data):
    counter = 0
    for line in data:
        out = line.split(" | ")[1]
        digits = out.split()
        for digit in digits:
            if len(digit) in unique:
                counter += 1
    return counter


def map_digits(digits):
    mapper = {}
    mapper["a"] = digits[1].difference(digits[0]).pop()
    mapper["bd"] = digits[2].difference(digits[0])
    mapper["eg"] = digits[9].difference(digits[1].union(digits[2]))

    mapper[1] = digits[0]
    mapper[7] = digits[1]
    mapper[4] = digits[2]
    mapper[8] = digits[9]
    for dig in digits[6:9]:
        c = digits[0].difference(dig)
        if c:
            mapper[6] = dig
            mapper["f"] = mapper[1].difference(c).pop()
            mapper["c"] = c.pop()

        elif not digits[2].difference(dig):
            mapper[9] = dig
            e = mapper[8].difference(dig)
            mapper["g"] = mapper["eg"].difference(e).pop()
            mapper["e"] = e.pop()

        else:
            mapper[0] = dig
            d = mapper[8].difference(dig)
            mapper["b"] = mapper["bd"].difference(d).pop()
            mapper["d"] = d.pop()

    mapper[2] = {mapper["a"], mapper["c"], mapper["d"], mapper["e"], mapper["g"]}
    mapper[3] = {mapper["a"], mapper["c"], mapper["d"], mapper["f"], mapper["g"]}
    mapper[5] = {mapper["a"], mapper["b"], mapper["d"], mapper["f"], mapper["g"]}

    return {frozenset(mapper[i]): i for i in range(10)}


def part2(data):
    counter = 0
    for line in data:
        split = line.split(" | ")
        ins = list(sorted(split[0].split(), key=len))
        outs = split[1].split()
        digits = map_digits([set(i) for i in ins])
        outs = [digits[frozenset(d)] for d in outs]
        counter += (outs[0] * 1000) + (outs[1] * 100) + (outs[2] * 10) + (outs[3])

    return counter


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()

        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
