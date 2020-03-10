dp = [[0] * 2 for _ in range(91)]
dp[1][1] = 1
dp[2][0] = 1
def main():
    num = int(input())
    for iter in range(3, num + 1):
        dp[iter][0] = dp[iter - 1][1] + dp[iter - 1][0]
        dp[iter][1] = dp[iter - 1][0]
    print(sum(dp[num]))
    return
main()