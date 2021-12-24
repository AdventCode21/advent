import sys

def parse_input():
    with open(sys.argv[1], 'r') as file:
        readings = [[int(i) for i in line if i != '\n'] for line in file.readlines()]
        return readings

def is_inside_borders(i, j, readings):
    return i >= 0 and i <= len(readings)-1 and j >= 0 and j <= len(readings[0])-1

def is_low_point(i, j, readings):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for (ix, jx) in steps:
        if is_inside_borders(i+ix, j+jx, readings):
            if readings[i][j] >= readings[i+ix][j+jx]:
                return False
    return True
    
def dfs(i, j, readings, size_of_basins, visited):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for (ix, jx) in steps:
        if is_inside_borders(i+ix, j+jx, readings) and readings[i+ix][j+jx] != 9 and readings[i][j] <= readings[i+ix][j+jx] and (i+ix, j+jx) not in visited:
            visited[(i+ix, j+jx)] = True
            size_of_basins[-1] += 1
            dfs(i+ix, j+jx, readings, size_of_basins, visited)

def ex1(readings):
    ans = 0
    for i in range(len(readings)):
        for j in range(len(readings[0])):
            if is_low_point(i, j, readings):
                ans += readings[i][j]+1
    return ans


def ex2(readings):
    size_of_basins = []
    visited = {}
    for i in range(len(readings)):
        for j in range(len(readings[0])):
            if is_low_point(i, j, readings):
                size_of_basins.append(1)
                dfs(i, j, readings, size_of_basins, visited)
    size_of_basins.sort(reverse=True)
    return size_of_basins[0] * size_of_basins[1] * size_of_basins[2]


if __name__ == "__main__":
    readings = parse_input()
    print(ex1(readings))
    print(ex2(readings))
