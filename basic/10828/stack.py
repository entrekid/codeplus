import sys
input = sys.stdin.readline
def main():
    test_case = int(input())
    stack = []
    size = 0
    for _ in range(test_case):
        order = input().rstrip().split()
        if order[0] == "push":
            stack.append(int(order[1]))
            size += 1
        if order[0] == "pop":
            if stack:
                print(stack.pop())
                size -= 1
            else:
                print(-1)
        if order[0] == "size":
            print(size)
        if order[0] == "empty":
            print(int(size == 0))
        if order[0] == "top":
            if stack:
                print(stack[size - 1])
            else:
                print(-1)

main()