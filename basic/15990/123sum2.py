import sys
input = sys.stdin.readline
div = 1000000009
dp = [[0] * 4 for _ in range(100001)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1
for iter in range(4, 100001):
    dp[iter][1] = (dp[iter - 1][2] + dp[iter - 1][3]) % div
    dp[iter][2] = (dp[iter - 2][1] + dp[iter - 2][3]) % div
    dp[iter][3] = (dp[iter - 3][1] + dp[iter - 3][2]) % div
def main():
    test_case = int(input())
    for _ in range(test_case):
        print(sum(dp[int(input())]) % div)
    return
main()