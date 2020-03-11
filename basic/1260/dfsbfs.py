import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().rstrip().split())
dfs_check = [False] * (n + 1)
bfs_check = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for elem in range(n):
    graph[elem].sort()
def dfs(start):
    dfs_check[start] = True
    print(start, end = " ")
    for elem in graph[start]:
        if not dfs_check[elem]:
            dfs(elem)
    return

def bfs(start):
    deq = deque()
    print(start, end = " ")
    bfs_check[start] = True
    deq.append(start)
    while deq:
        basis = deq.popleft()
        for elem in graph[basis]:
            if not bfs_check[elem]:
                bfs_check[elem] = True
                print(elem, end = " ")
                deq.append(elem)
    return

dfs(v)
print()
bfs(v)
print()