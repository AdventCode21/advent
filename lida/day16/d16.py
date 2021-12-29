import os.path
import time
import math


def zero(packets):
    return sum(packets)


def one(packets):
    return math.prod(packets)


def two(packets):
    return min(packets)


def three(packets):
    return max(packets)


def four(packet):
    last = "1"
    num = ""
    i = 0
    while last == "1":
        last = packet[i]
        num += packet[i + 1 : i + 5]
        i += 5

    return 0, int(num, 2), packet[i:]


def five(packets):
    if packets[0] > packets[1]:
        return 1
    else:
        return 0


def six(packets):
    if packets[0] < packets[1]:
        return 1
    else:
        return 0


def seven(packets):
    if packets[0] == packets[1]:
        return 1
    else:
        return 0


def totalength(packets, operation):
    n = int(packets[:15], 2)

    packet = packets[15 : 15 + n]
    decoded = []
    versions = 0
    while packet:
        v, d, packet = decode(packet)
        decoded.append(d)
        versions += v
    result = globals()[operation](decoded)
    return versions, result, packets[15 + n :]


def totalnumber(packets, operation):
    n = int(packets[:11], 2)
    packet = packets[11:]
    decoded = []
    versions = 0
    for _ in range(n):
        v, d, packet = decode(packet)
        decoded.append(d)
        versions += v
    result = globals()[operation](decoded)
    return versions, result, packet


def decode(packet):

    mapper = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        5: "five",
        6: "six",
        7: "seven",
    }
    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)
    if type_id == 4:
        v, result, rest = four(packet[6:])
    else:
        if packet[6] == "1":
            v, result, rest = totalnumber(packet[7:], mapper[type_id])

        elif packet[6] == "0":
            v, result, rest = totalength(packet[7:], mapper[type_id])

    versions = version + v
    return versions, result, rest


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = "".join([format(int(char, 16), "04b") for char in f.read()])
        versions, result, _ = decode(data)
        print(f"Part 1: {versions}")
        print(f"Part 2: {result}")

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
