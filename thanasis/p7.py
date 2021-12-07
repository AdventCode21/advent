import sys
import numpy as np

def parse_input():
    with open(sys.argv[1]) as file:
        return [int(i) for i in file.readlines()[0].split(',')]

def ex1(initial_positions):
    min_cost = np.inf
    for current_position in range(min(initial_positions), max(initial_positions)+1):
        current_cost = sum([abs(pos - current_position) for pos in initial_positions])
        min_cost = min(current_cost, min_cost)
    return min_cost 

def ex2(initial_positions):
    min_cost = np.inf
    for current_position in range(min(initial_positions), max(initial_positions)+1):
        current_cost = sum([abs(pos - current_position)*(abs(pos - current_position) + 1)//2 for pos in initial_positions])
        min_cost = min(current_cost, min_cost)
    return min_cost 


if __name__ == "__main__":
    initial_positions = parse_input()
    print(ex1(initial_positions))
    print(ex2(initial_positions))
