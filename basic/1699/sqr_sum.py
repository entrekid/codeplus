"""
dp_list[num] = num을 만들기 위한 최소한의 제곱수
"""
def main():
    num = int(input())
    dp = [-1] * (num + 1)
    # dp[iter] = dp[iter - 0] dp[iter - 1] dp[iter - 2] dp[iter - 3]
    basis = int(num ** 2)
    