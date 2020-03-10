import sys
input = sys.stdin.readline
from collections import deque
"""
a진법 b진법이고 모두 2이상 30이하의 자연수
입력의 두 번째 줄에는 a진법으로 나타낸 숫자의 자리수의 개수
세 번째 수는 각 자리를 이루고 있는 숫자들
"""
def main():
    base_a, base_b = map(int, input().split())
    length = int(input())
    num = list(map(int, input().rstrip().split()))
    basis = 0
    ans = deque()
    for elem in num:
        basis *= base_a
        basis += elem
    while basis:
        ans.appendleft(str(basis % base_b))
        basis = basis // base_b
    print(" ".join(ans))
    return
main()
