import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1
check = [False] * n
cnt = 0
def dfs(depth, start):
    global cnt
    if depth == 4:
        check[start] = True
        cnt += 1
        return
    else:
        check[start] = True
        for iter in range(n):
            if not check[iter] and graph[start][iter]:
                check[iter] = True
                dfs(depth + 1, iter)
                check[iter] = False
        check[start] = False

for iter in range(n):
    dfs(0, iter)
    if cnt:
        print(1)
        break
else:
    print(0)