import sys
from collections import deque
input = sys.stdin.readline

def main():
    test_case = int(input())
    queue = deque()
    size = 0
    for _ in range(test_case):
        order = input().rstrip().split()
        if order[0] == "push":
            queue.append(int(order[1]))
            size += 1
        elif order[0] == "pop":
            if queue:
                print(queue.popleft())
                size -= 1
            else:
                print(-1)
        elif order[0] == "size":
            print(size)
        elif order[0] == "empty":
            print(int(size == 0))
        elif order[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        else:
            if queue:
                print(queue[size - 1])
            else:
                print(-1)

main()
            