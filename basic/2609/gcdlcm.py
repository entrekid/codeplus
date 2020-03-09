import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def main():
    a, b = map(int, input().rstrip().split())
    num_gcd = gcd(a, b)
    num_lcm = a * b // num_gcd
    print(num_gcd)
    print(num_lcm)
    return

main()