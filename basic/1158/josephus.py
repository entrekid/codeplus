import sys
from collections import deque
input = sys.stdin.readline
"""
1, 2, 3, 4, 5, 6, 7
"""

def main():
    n, k = map(int, input().rstrip().split())
    queue = deque(range(1, n + 1))
    ans = []
    while queue:
        queue.rotate(-(k - 1))
        ans.append(queue.popleft())
    print("<", end = "")
    print(*ans, sep = ", ", end = ">\n")
main()

