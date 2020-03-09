import sys
from collections import deque
input = sys.stdin.readline

def main():
    test_case = int(input())
    dequeue = deque()
    size = 0
    for _ in range(test_case):
        order = input().rstrip().split()
        if order[0] == "push_front":
            dequeue.appendleft(int(order[1]))
        elif order[0] == "push_back":
            dequeue.append(int(order[1]))
        elif order[0] == "pop_front":
            print(dequeue.popleft() if dequeue else -1)
        elif order[0] == "pop_back":
            print(dequeue.pop() if dequeue else -1)
        elif order[0] == "size":
            print(len(dequeue))
        elif order[0] == "empty":
            print(int(len(dequeue) == 0))
        elif order[0] == "front":
            print(dequeue[0] if dequeue else -1)
        else:
            print(dequeue[-1] if dequeue else -1)
            

main()