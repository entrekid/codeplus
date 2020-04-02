# linked list
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False] * (N + 1)
check[0] = True
def dfs(start):
    check[start] = True
    for elem in graph[start]:
        if not check[elem]:
            dfs(elem)
cnt = 0
for iter in range(1, N + 1):
    if not check[iter]:
        dfs(iter)
        cnt += 1
print(cnt)
