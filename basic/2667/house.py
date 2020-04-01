import sys
input = sys.stdin.readline
num = int(input())
graph = [list(input().rstrip()) for _ in range(num)]
print(graph)