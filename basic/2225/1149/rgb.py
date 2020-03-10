import sys
input = sys.stdin.readline
def main():
    test_case = int(input())
    dp = [[0, 0, 0] for _ in range(test_case)]
    for iter in range(test_case):
        a, b, c = map(int, input().rstrip().split())
        if iter == 0:
            dp[iter][0] = a
            dp[iter][1] = b
            dp[iter][2] = c
        else:
            dp[iter][0] = a + min(dp[iter - 1][1], dp[iter - 1][2])
            dp[iter][1] = b + min(dp[iter - 1][2], dp[iter - 1][0])
            dp[iter][2] = c + min(dp[iter - 1][0], dp[iter - 1][1])
    print(min(dp[test_case - 1]))
    return
main()