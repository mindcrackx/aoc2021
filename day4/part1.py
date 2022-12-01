import re
import sys

data = open("input.txt", "r", encoding="utf-8").read().splitlines()


def print_board(board):
    for line in board:
        print(line)


def calculate_score(board, final_num):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if not board[row][col][1]:
                score += board[row][col][0]
    return score * final_num


nums = [int(x) for x in data[0].split(",")]

boards = []
board = []
for line in data[2:]:
    if line == "":
        boards.append(board)
        board = []
        continue
    board.append([(int(x), False) for x in re.split("\s+", line.strip())])
boards.append(board)


for num in nums:
    for board in boards:
        for row_i, row in enumerate(board):
            for col_i, col in enumerate(row):
                if col[0] == num:
                    board[row_i][col_i] = (col[0], True)
    for board in boards:
        for row in range(len(board)):
            count = 0
            for col in range(len(board[row])):
                if board[row][col][1]:
                    count += 1
                if count == 5:
                    print(calculate_score(board, num))
                    sys.exit(0)
        for col in range(len(board[row])):
            count = 0
            for row in range(len(board)):
                if board[row][col][1]:
                    count += 1
                if count == 5:
                    print(calculate_score(board, num))
                    sys.exit(0)
