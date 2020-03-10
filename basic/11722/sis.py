def main():
    num = int(input())
    num_list = list(map(int, input().split()))
    dp = [1] * num
    for iter in range(num):
        for jter in range(iter):
            if num_list[iter] < num_list[jter] and dp[iter] < dp[jter] + 1:
                dp[iter] = dp[jter] + 1
    print(max(dp))
    return
main()