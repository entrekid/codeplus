from collections import deque
q = deque()
MAX = 200001
n, m = map(int, input().split())
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
check[n] = True
dist[n] = 0
q.append(n)
while q:
    point = q.popleft()
    for nxt in [point - 1, point + 1, point * 2]:
        if 0 <= nxt <= MAX and check[nxt] == False:
            check[nxt] = True
            dist[nxt] = dist[point] + 1
            q.append(nxt)
print(dist[m])