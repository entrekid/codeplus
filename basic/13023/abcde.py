import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
cnt = 0
check = [False] * n
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for iter in range(n):
    graph[iter].sort()
def dfs(depth, start):
    global cnt
    if depth == 4:
        check[start] = True
        cnt += 1
        return
    else:
        check[start] = True
        for elem in graph[start]:
            if not check[elem]:
                dfs(depth + 1, elem)
        check[start] = False
    return
for elem in range(n):
    dfs(0, elem)
    if cnt:
        print(1)
        break
if not cnt:
    print(0)

