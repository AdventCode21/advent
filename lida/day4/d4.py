import time
from collections import defaultdict


with open("data_d4.txt") as f:
    data = f.read().splitlines()
    draws = data.pop(0).split(",")
    i = 0
    board = []
    boards = {}
    for line in data[1:]:
        if line:
            board.extend(line.split())
        else:
            boards[i] = board
            i += 1
            board = []
    if board:
        boards[i] = board


def check(board):
    for i in range(5):
        if not (
            board[i * 5 + 0]
            or board[i * 5 + 1]
            or board[i * 5 + 2]
            or board[i * 5 + 3]
            or board[i * 5 + 4]
        ):
            return True
        if not (
            board[i + 0]
            or board[i + 5]
            or board[i + 10]
            or board[i + 15]
            or board[i + 20]
        ):
            return True

    if not (board[0] or board[6] or board[12] or board[18] or board[24]):
        return True
    if not (board[4] or board[8] or board[12] or board[16] or board[20]):
        return True

    return False


def cross(number):
    winners = []
    for i in boards:
        board = boards[i]
        boards[i] = [None if x == number else x for x in board]

        if check(boards[i]):
            winners.append((i, sum([int(x) for x in boards[i] if x]) * int(number)))

    return winners


def d4_p1():
    for draw in draws:
        winners = cross(draw)
        if winners:
            return winners[0][1]

    return 0


def d4_p2():
    for draw in draws:
        winners = cross(draw)
        for winner in winners:
            del boards[winner[0]]
        if len(boards) == 0:
            return winners[-1][1]
    return 0


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    print(d4_p1())
    print(d4_p2())

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
