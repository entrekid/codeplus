import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def main():
    n, s = map(int, input().rstrip().split())
    kid_list = list(map(int, input().rstrip().split()))
    num_list = []
    for elem in kid_list:
        num_list.append(abs(elem - s))
    no_gcd = num_list[0]
    for elem in num_list:
        no_gcd = gcd(elem, no_gcd)
    print(no_gcd)
    return
main()