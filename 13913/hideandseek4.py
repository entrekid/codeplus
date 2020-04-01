from collections import deque
n, m = map(int, input().split())
MAX = 200000
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
fro = [-1] * (MAX + 1)
check[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    here = q.popleft()
    for nxt in [here - 1, here + 1, here * 2]:
        if 0 <= nxt <= MAX and check[nxt] == False:
            dist[nxt] = dist[here] + 1
            check[nxt] = True
            fro[nxt] = here
            q.append(nxt)
# find a path
stack = deque()
base = m
while base != -1:
    stack.append(base)
    base = fro[base]   
print(dist[m])
while stack:
    print(stack.pop(), end = " ")
print()