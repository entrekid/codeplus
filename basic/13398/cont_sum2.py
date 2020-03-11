"""
d[i] = i번째에서 끝나는 연속합
d2[i] = i번째에서 시작하는 연속합

"""
num = int(input())
num_list = list(map(int, input().split()))
dp1 = [0] * num
dp2 = [0] * num
for iter in range(num):
    dp1[iter] = num_list[iter]
    if iter == 0:
        continue
    if dp1[iter] < dp1[iter - 1] + num_list[iter]:
        dp1[iter] = dp1[iter - 1] + num_list[iter]

for iter in range(num - 1, -1, -1):
    dp2[iter] = num_list[iter]
    if iter == num - 1:
        continue
    if dp2[iter + 1] + num_list[iter] > dp2[iter]:
        dp2[iter] = dp2[iter + 1] + num_list[iter]
dp = [0] * num
dp[0] = dp2[0]
for iter in range(1, num - 1):
    dp[iter] = dp1[iter - 1] + dp2[iter + 1]
dp[num-1] = dp1[num - 1]
ans = max(dp)
ans2 = max(dp1)
print(ans if ans > ans2 else ans2)