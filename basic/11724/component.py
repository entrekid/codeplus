import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
check = [False] * (n)
def dfs(start):
    check[start] = True
    for elem in graph[start]:
        if not check[elem]:
            dfs(elem)
cnt = 0
for iter in range(n):
    if not check[iter]:
        dfs(iter)
        cnt += 1
print(cnt)