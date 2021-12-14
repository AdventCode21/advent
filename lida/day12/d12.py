import os.path
import time
from collections import defaultdict


def part1(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if (node.islower() and node not in path) or node.isupper():
            newpaths = part1(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def part2(graph, start, end, path=[], twice=False):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.islower() and node in path:
            if twice or node == "start":
                continue
            else:
                newpaths = part2(graph, node, end, path, True)
        else:
            newpaths = part2(graph, node, end, path, twice)
        for newpath in newpaths:
            paths.append(newpath)
    return paths


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()
        nodes = defaultdict(list)
        for line in data:
            n = line.split("-")
            nodes[n[0]].append(n[1])
            nodes[n[1]].append(n[0])

        print(len(part1(nodes, "start", "end")))
        print(len(part2(nodes, "start", "end")))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
