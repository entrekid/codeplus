import sys
input = sys.stdin.readline
def main():
    num = int(input())
    tri = [[0] * num for _ in range(num)]
    for iter in range(num):
        num_list = map(int, input().rstrip().split())
        base = 0
        for elem in num_list:
            tri[iter][base] = elem
            base += 1
    dp = [[0] * num for _ in range(num)]
    dp[0][0] = tri[0][0]
    """
    dp[m][n] = dp[m-1][n] + dp[m-1][n - 1] 중 큰 것과 tri[m][n]
    맨 좌측 끝일 때 : dp[m][0] 만 올 수 있음
    맨 우측 끝일 때 : dp[m][n-1]만 올 수 있는데 어차피 0이므로 상관 없음
    """ 
    # 좌측 끝 정리
    for iter in range(1, num):
        dp[iter][0] = dp[iter - 1][0] + tri[iter][0]
    # 나머지 정리
    for iter in range(1, num):
        for jter in range(1, iter + 1):
            dp[iter][jter] = + tri[iter][jter] + max(dp[iter - 1][jter], dp[iter - 1][jter - 1]) 
    print(max(dp[num - 1]))
    return
main()