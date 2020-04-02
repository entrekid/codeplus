import sys
input = sys.stdin.readline
from collections import deque
N, M, start = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

check1 = [False] * (N + 1)
check1[0] = True
def dfs(start):
    check1[start] = True
    print(start, end = " ")
    for iter in range(N + 1):
        if not check1[iter] and graph[start][iter]:
            check1[iter] = True
            dfs(iter)

dfs(start)
print()
check2 = [False] * (N + 1)
check2[0] = True
def bfs(start):
    queue = deque()
    queue.append(start)
    check2[start] = True
    while queue:
        basis = queue.popleft()
        print(basis, end = " ")
        for iter in range(N + 1):
            if not check2[iter] and graph[basis][iter]:
                check2[iter] = True
                queue.append(iter)

bfs(start)
print()


