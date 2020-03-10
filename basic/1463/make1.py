dp = [0] * 1000001
def main():
    num = int(input())
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for iter in range(4, num + 1):
        dp[iter] = dp[iter - 1] + 1
        if iter % 2 == 0:
            dp[iter] = min(dp[iter] - 1, dp[iter // 2]) + 1
        if iter % 3 == 0:
            dp[iter] = min(dp[iter] - 1, dp[iter // 3]) + 1
    print(dp[num])
    return

main()