num = int(input())
num_list = list(map(int, input().split()))
dp_inc = [0] * num
dp_dec = [0] * num
for iter in range(num):
    dp_inc[iter] = 1
    for jter in range(iter):
        if num_list[iter] > num_list[jter] and dp_inc[iter] < dp[jter] + 1:
            dp[iter] = dp[jter] + 1
for iter in range(num - 1, -1, -1):
    dp_dec[iter] = 1
    for jter in range(iter + 1, num):
        if num_list[iter] > num_list[jter] and dp_dec[jter] + 1 > dp_dec[iter]:
            dp_dec[iter] = dp_dec[jter] + 1
dp = [dp_inc[iter] + dp_dec[iter] - 1 for iter in range(num)]
print(max(dp))