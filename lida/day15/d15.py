import copy
import os.path
import time
from collections import defaultdict
from queue import PriorityQueue
import numpy as np


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = defaultdict(lambda: -1)
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[(u, v)] = weight


def dijkstra(graph, neighbors, start_vertex):
    D = defaultdict(lambda: float("inf"))
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in neighbors[current_vertex]:
            if graph.edges[(current_vertex, neighbor)] != -1:
                distance = graph.edges[(current_vertex, neighbor)]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def find_neighbors(point, rows, cols):
    return [
        (x0, y0)
        for x0 in range(point[0] - 1, point[0] + 2)
        for y0 in range(point[1] - 1, point[1] + 2)
        if (
            (point[0] != x0 or point[1] != y0)
            and (0 <= x0 < rows)
            and (0 <= y0 < cols)
            and abs(x0 - point[0] + y0 - point[1]) == 1
        )
    ]


def create_graph(data):
    g = Graph(len(data) * len(data[0]))
    neighbors = {}
    for x in range(len(data)):
        for y in range(len(data[0])):
            neighbors[(x, y)] = find_neighbors((x, y), len(data), len(data[0]))

            for neighbor in neighbors[(x, y)]:
                weight = data[neighbor[0]][neighbor[1]]
                g.add_edge((x, y), neighbor, weight)
    return g, neighbors


def create_map(data):
    current = {}
    current[0] = data
    for i in range(8):
        current[i + 1] = [[j + 1 if j < 9 else 1 for j in line] for line in current[i]]
    rows = []
    for i in range(5):
        rows.append(
            np.concatenate([current[j] for j in range(i, i + 5)], axis=1, out=None)
        )
    return np.concatenate(rows, axis=0).tolist()


def part1(data):

    g, neighbors = create_graph(data)
    print("graph created")
    distances = dijkstra(g, neighbors, (0, 0))
    return distances[(len(data) - 1, len(data[0]) - 1)]


def part2(data):

    full = create_map(data)
    print("map created")
    return part1(full)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [[int(char) for char in line] for line in f.read().splitlines()]

        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
