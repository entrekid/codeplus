import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

check = [False] * (N + 1)
check[0] = True
def dfs(start):
    check[start] = True
    for iter in range(N + 1):
        if not check[iter] and graph[iter][start]:
            check[iter] = True
            dfs(iter)
cnt = 0
for iter in range(1, N + 1):
    if not check[iter]:
        dfs(iter)
        cnt += 1
print(cnt)