import sys
input = sys.stdin.readline
dp = [0] * 1001
def main():
    num = int(input())
    num_list = [0] + list(map(int, input().rstrip().split()))
    dp[1] = num_list[1]
    for iter in range(2, num + 1):
        dp[iter] = num_list[iter]
        for jter in range(1, iter + 1):
            dp[iter] = min(dp[iter], dp[iter - jter] + num_list[jter])
    print(dp[num])
    return
main()
"""
-1 초기화 일 때

n = int(input())
a = [0] + list(map(int, input().split()))
d = [-1] * (n + 1)
d[0] = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if d[i] == -1 or d[i] > d[i-j] + a[j]:
            d[i] = d[i-j] + a[j]
print(d[n])
"""