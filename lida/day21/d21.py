import functools
import os.path
import time


def part1(player1, player2):
    dice = 0
    score1 = 0
    score2 = 0
    round = 0
    while score1 < 1000 and score2 < 1000:
        if round % 2 == 0:
            player1 += (3 * dice) + 1 + 2 + 3
            player1 = player1 % 10 if player1 % 10 else 10
            score1 += player1
        else:
            player2 += (3 * dice) + 1 + 2 + 3
            player2 = player2 % 10 if player2 % 10 else 10
            score2 += player2
        dice += 3
        round += 1
    return round * 3 * min(score1, score2)


def normalise(pos):
    return pos % 10 if pos % 10 else 10


# def part2(player1,player2):
#     positions = {1:[player1],2:[player2]}
#     wins = {1:0,2:0}
#     scores = {1:[0],2:[0]}
#     lengths = len(scores[1])
#     rolling = 1
#     #combinations = list(itertools.product(*[[1,2,3],[1,2,3],[1,2,3]]))
#     combinations = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))
#     while lengths:
#         other = 3 - rolling
#         for i in range(lengths):
#             pos = positions[rolling][i]
#             score = scores[rolling][i]
#             pos2 = positions[other][i]
#             score2 = scores[other][i]
#             for comb, n in combinations:
#                 pos = normalise(pos + comb)
#                 if score + pos < 21:
#                     for _ in range(n):
#                         positions[rolling].append(pos)
#                         scores[rolling].append(score + pos)
#                         positions[other].append(pos2)
#                         scores[other].append(score2)
#                 else:
#                     wins[rolling] += n
#         l = len(scores[rolling])
#         positions[rolling] = positions[rolling][lengths:]
#         positions[other] = positions[other][lengths:]
#         scores[rolling] = scores[rolling][lengths:]
#         scores[other] = scores[other][lengths:]
#         lengths = len(scores[rolling])
#         rolling = 3 - rolling
#     return wins


@functools.lru_cache()
def score(player1, player2, score1=0, score2=0):
    wins1 = wins2 = 0
    for s, times in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
        pos = normalise(player1 + s)
        if score1 + pos < 21:
            w2, w1 = score(player2, pos, score2, score1 + pos)
            wins1 += w1 * times
            wins2 += w2 * times
        else:
            wins1 += times
    return wins1, wins2


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = f.read().splitlines()
        player1 = int(data[0].split(": ")[-1])
        player2 = int(data[1].split(": ")[-1])

        print(part1(player1, player2))
        print(max(score(player1, player2)))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
