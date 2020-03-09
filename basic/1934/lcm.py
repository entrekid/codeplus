import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def main():
    test_case = int(input())
    for _ in range(test_case):
        a, b = map(int, input().rstrip().split())
        num_gcd = gcd(a, b)
        print(a * b // num_gcd)
    return

main()