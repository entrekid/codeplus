"""
순회를 시작하는데 만약에 현재 컬러와 다른 것으로 순차적으로 탐험

"""
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    v,e = map(int, input().split())
    color = [0] * v
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for iter in range(v):
        graph[iter].sort()
    def dfs(start, c):
        color[start] = c
        for iter in graph[start]:
            if not color[iter]:
                dfs(iter, 3 - c)
    for iter in range(v):
        if not color[iter]:
            dfs(iter, 1)
    
    ans = True
    for iter in range(v):
        for elem in graph[iter]:
            if color[iter] == color[elem]:
                ans = False
                break
    print("YES" if ans else "NO")
