import sys
input = sys.stdin.readline
from collections import deque
N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for iter in range(N):
    graph[iter].sort()
check1 = [False] * (N + 1)
def bfs(start):
    queue = deque()
    queue.append(start)
    check1[start] = True
    while queue:
        basis = queue.popleft()
        print(basis, end = " ")
        for elem in graph[basis]:
            if not check1[elem]:
                check1[elem] = True
                queue.append(elem)

check2 = [False] * (N + 1)
def dfs(start):
    check2[start] = True
    print(start, end = " ")
    for elem in graph[start]:
        if not check2[elem]:
            dfs(elem)
dfs(start)
print()
bfs(start)
print()