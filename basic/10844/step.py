import sys
input = sys.stdin.readline
div = 1000000000
dp = [[0] * 10 for _ in range(101)]
for iter in range(1, 10):
    dp[1][iter] = 1
dp[2][0] = dp[1][1]
dp[2][1] = dp[1][2]
dp[2][9] = dp[1][8]
for iter in range(2, 9):
    dp[2][iter] = (dp[1][iter - 1] + dp[1][iter + 1])
def main():
    num = int(input())
    for iter in range(3, num + 1):
        dp[iter][0] = dp[iter - 1][1]
        dp[iter][9] = dp[iter - 1][8]
        for jter in range(1, 9):
            dp[iter][jter] = (dp[iter - 1][jter - 1] + dp[iter - 1][jter + 1]) % div
    print(sum(dp[num]) % div)
main()
