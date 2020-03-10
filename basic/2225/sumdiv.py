"""
dp[n][k] = dp[n - 1][k - 1] + dp[n - 2][k - 1] + - - - + dp[0][k - 1]

"""
dp = [[0] * 201 for _ in range(201)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
div = 1000000000

def main():
    n, k = map(int, input().split())
    for iter in range(3, n + 1):
        for jter in range(1, k + 1):
            for lter in range(0, iter + 1):
                dp[iter][jter]  += dp[iter - lter][jter - 1] % div
    
    print(dp[n][k])
main()