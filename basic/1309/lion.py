div = 9901
dp = [[0, 0, 0] for _ in range(100000)]
def main():
    num = int(input())
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1
    for iter in range(1, num):
        dp[iter][0] = (dp[iter - 1][1] + dp[iter - 1][2]) % div
        dp[iter][1] = (dp[iter - 1][0] + dp[iter - 1][2]) % div
        dp[iter][2] = (sum(dp[iter - 1])) % div
    print(sum(dp[num - 1]) % div)
main()