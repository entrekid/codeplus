import sys
input = sys.stdin.readline
"""

"""
def check(string):
    ans = 0
    stack = []
    size = 0
    for iter in range(len(string)):
        if string[iter] == "(":
            stack.append(iter)
            size += 1
        else: # string[iter] == ")"
            if stack[-1] + 1 == iter: # rasor
                stack.pop()
                size -= 1
                ans += size
            else: # stick
                stack.pop()
                size -= 1
                ans += 1
    return ans

def main():
    ps = input().rstrip()
    print(check(ps))
    return

main()