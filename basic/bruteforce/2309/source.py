import sys
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
total = sum(a)
for i in range(0, n):
    for j in range(i + 1, n):
        if total - 100 == (a[i] + a[j]):
            for k in range(n):
                if k == i or k == j:
                    continue
                print(a[k])
            sys.exit()