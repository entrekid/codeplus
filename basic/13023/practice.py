import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
check = [False] * n
cnt = 0
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for iter in range(n):
    graph[iter].sort()

def dfs(depth, start):
    global cnt
    if depth == 4:
        cnt += 1
        return
    else:
        check[start] = True
        for iter in graph[start]:
            if not check[iter]:
                check[iter] = True
                dfs(depth + 1, iter)
                check[iter] = False
        check[start] = False

for iter in range(n):
    dfs(0, iter)
    if cnt:
        print(1)
        break
if not cnt:
    print(0) 
