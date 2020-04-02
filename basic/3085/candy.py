import sys
input = sys.stdin.readline

def count_point(board):
    num_max = 0
    for row in board:
        for col in board:

num = int(input())
board = [list(input().rsplit()) for _ in range(num)]
