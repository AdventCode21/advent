import sys
import copy

def parse_input():
    with open(sys.argv[1], 'r') as file:
        octopuses = [[int(i) for i in line if i != '\n'] for line in file.readlines()]
        return octopuses

def is_inside_borders(i, j, octopuses):
    return 0 <= i <= len(octopuses)-1 and 0 <= j <= len(octopuses[0])-1

def flash(i, j, octopuses, flashes, flash_flags, episode_flashes, part_1):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for (ix, jx) in steps:
        if is_inside_borders(i+ix, j+jx, octopuses):
            if (i+ix, j+jx) not in flash_flags:
                octopuses[i+ix][j+jx] += 1
            if octopuses[i+ix][j+jx] == 10:
                episode_flashes += 1
                flash_flags.add((i+ix, j+jx))
                octopuses[i+ix][j+jx] = 0
                flashes, episode_flashes = flash(i+ix, j+jx, octopuses, flashes+1, flash_flags, episode_flashes, part_1)
                if episode_flashes == len(octopuses) * len(octopuses[0]) and not part_1:
                    return flashes, episode_flashes
    return flashes, episode_flashes

def ex(octopuses, part_1):
    flashes = 0
    step = 0
    while True:
        step += 1
        if step == 101 and part_1:
            break
        episode_flashes = 0
        flash_flags = set() 
        for i in range(len(octopuses)):
            for j in range(len(octopuses[0])):
                if (i, j) not in flash_flags:
                    octopuses[i][j] += 1
                if octopuses[i][j] == 10:
                    flash_flags.add((i, j))
                    episode_flashes += 1
                    octopuses[i][j] = 0
                    flashes, episode_flashes = flash(i, j, octopuses, flashes+1, flash_flags, episode_flashes, part_1)
                    if episode_flashes == len(octopuses) * len(octopuses[0]) and not part_1:
                        return step
    return flashes

if __name__ == "__main__":
    octopuses = parse_input()
    print(ex(octopuses, True))
    octopuses = parse_input()
    print(ex(octopuses, False))