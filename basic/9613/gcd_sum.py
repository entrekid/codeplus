import sys
input = sys.stdin.readline
from collections import deque
def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def main():
    test_case = int(input())
    for _ in range(test_case):
        num_list = deque(map(int, input().rstrip().split()))
        num_list.popleft()
        length = len(num_list)
        gcd_list = []
        for iter in range(length):
            for jter in range(iter + 1, length):
                gcd_list.append(gcd(num_list[iter], num_list[jter]))
        print(sum(gcd_list))
    return

main() 