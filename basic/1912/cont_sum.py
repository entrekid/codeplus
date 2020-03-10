"""
dp[n] : n번째 숫자 포함되었을 때의 최댓값
dp[n-1] + p[n]과 p[n] 사이에서 비교
"""
def main():
    num = int(input())
    num_list = list(map(int, input().split()))
    dp_list = [0] * num
    dp_list[0] = num_list[0]
    for iter in range(1, num):
        dp_list[iter] = max(dp_list[iter - 1] + num_list[iter], num_list[iter])
    print(max(dp_list))
    return
main()

    