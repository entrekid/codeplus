import sys
input = sys.stdin.readline
from collections import deque

"""
AB|CD
"""
def main():
    left = deque(input().rstrip())
    right = deque()
    test_case = int(input())    
    for _ in range(test_case):
        order = input().rstrip().split()
        if order[0] == "L":
            if left:
                right.appendleft(left.pop())
        elif order[0] == "D":
            if right:
                left.append(right.popleft())
        elif order[0] == "B":
            if left:
                left.pop()
        else:
            left.append(order[1])
    print("".join(left) + "".join(right))
    return
    
main()