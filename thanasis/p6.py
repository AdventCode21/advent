import sys
import time

def parse_input():
    with open(sys.argv[1]) as file:
        return [int(i) for i in file.readlines()[0].split(',')]

# fast
def ex2(state):
    days_to_fishes = {i : 0 for i in range(-1, 9)}
    for day in state:
        days_to_fishes[day] += 1
    for _ in range(256):
        days_to_fishes = {i-1 : days_to_fishes[i] for i in range(9)}
        new_fishes = days_to_fishes[-1]
        days_to_fishes[8] = new_fishes
        days_to_fishes[6] += new_fishes
    return sum(days_to_fishes.values()) - days_to_fishes[-1]

# slow
def ex1(state, count=0):
    if count == 80:
        return len(state)
    current_length = len(state)
    for i in range(current_length):
        if state[i] == 0:
            state[i] = 6
            state.append(8)
        else:
            state[i] -= 1
    return ex1(state, count+1) 

if __name__ == "__main__":
    init_state = parse_input()
    start_time = time.time()
    print(ex1(init_state))
    print(ex2(init_state))
    print(f'Total elapsed time: {time.time() - start_time} secs')
