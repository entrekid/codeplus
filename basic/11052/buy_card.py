import sys
input = sys.stdin.readline

dp = [0] * 10001
def main():
    num = int(input())
    num_list = [0] + list(map(int, input().rstrip().split()))
    dp[1] = num_list[1]
    ret = dp[1]
    for iter in range(2, num + 1):
        for jter in range(1, iter + 1):
            dp[iter] = max(dp[iter], dp[iter - jter] + num_list[jter])
        ret = max(dp[iter], dp[iter - 1])
    print(ret)
    return
main()