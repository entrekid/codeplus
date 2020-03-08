import sys
input = sys.stdin.readline
from collections import deque
"""
input이
stack의 마지막 수보다 큰 경우
    stack의 마지막 수부터 input까지 append하고 +를 포함
    같아지는 순간 -하고 stack에서 pop 
stack의 마지막 수보다 작은 경우
    return NO
stack의 마지막 수와 같은 경우
    -하고 stack에서 pop
"""
def main():
    num = int(input())
    stack = []
    num_list = deque(range(1, num + 1))
    ans = []
    for _ in range(num):
        check = int(input())
        if stack:
            basis = stack[-1]
            if basis > check:
                print("NO")
                return
            elif basis == check:
                stack.pop()
                ans.append("-")
            else: # stack[-1] < check
                while True:
                    if basis == check:
                        break
                    stack.append(num_list.popleft())
                    ans.append("+")
                    basis = stack[-1]
                stack.pop()
                ans.append("-")
        else:
            # stack이 비었을 때 현재 수까지 append 해야함  
            while True:
                stack.append(num_list.popleft())
                ans.append("+")
                basis = stack[-1]
                if basis == check:
                    break
            stack.pop()
            ans.append("-")
    print(*ans, sep = "\n", end = "\n")

main()