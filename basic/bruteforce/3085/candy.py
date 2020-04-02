import sys
input = sys.stdin.readline
size = int(input())
board = [list(input().rstrip()) for _ in range(size)]
print(board)