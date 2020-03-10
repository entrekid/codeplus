div = 10007
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
def main():
    num = int(input())
    for iter in range(3, num + 1):
        dp[iter] = (2 * dp[iter - 2] + dp[iter - 1]) % div
    print(dp[num])
    return
main()