import os.path
import time

import numpy as np


def find_neighbors(point, rows, cols):
    return [
        (x0, y0)
        for x0 in range(point[0] - 1, point[0] + 2)
        for y0 in range(point[1] - 1, point[1] + 2)
        if ((0 <= x0 < rows) and (0 <= y0 < cols))
    ]


def bigger_picture(data, pw):
    p = np.array(data)
    p = np.pad(p, pad_width=2 * pw)
    return p


def binatodeci(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


def enhance(data, enhancement, rounds):
    picture = bigger_picture(data, rounds)
    rows, cols = picture.shape
    enhanced = np.copy(picture)
    for round in range(rounds):
        for i in range(rows):
            for j in range(cols):
                neighbors = find_neighbors((i, j), rows, cols)
                if len(neighbors) == 9:
                    binary = [picture[i[0]][i[1]] for i in neighbors]
                    index = binatodeci(binary)
                    enhanced[i][j] = enhancement[index]
                else:
                    if enhancement[0] == 1 and enhancement[-1] == 0:
                        if round % 2 == 0:
                            enhanced[i][j] = 1
                        else:
                            enhanced[i][j] = 0
        picture = np.copy(enhanced)

    return np.count_nonzero(picture == 1)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()
        enhancement = [0 if char == "." else 1 for char in data[0]]
        data = [[0 if char == "." else 1 for char in line] for line in data[2:]]

        print(enhance(data, enhancement, 2))
        print(enhance(data, enhancement, 50))
    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
