import sys
input = sys.stdin.readline
def main():
    length = int(input())
    num_list = list(map(int, input().rstrip().split()))
    # dp[n] : n번째 까지의 최대 합
    dp = [0] * length
    dp[0] = num_list[0]
    for iter in range(1, length):
        dp[iter] = num_list[iter]
        for jter in range(iter):
            if dp[iter] < dp[jter] + num_list[iter] and num_list[iter] > num_list[jter]:
                dp[iter] = dp[jter] + num_list[iter]
    print(max(dp))
    return
main()