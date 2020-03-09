import sys
input = sys.stdin.readline
print = sys.stdout.write

priority = {"*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 0}

def solve(string):
    stack = []
    for elem in string:
        if "A" <= elem <= "Z":
            print(elem)
        elif elem == "(":
            stack.append(elem)
        elif c == ")":
            while stack and stack[-1] != "(":
                print(stack.pop())
            stack.pop()
        else:
            while stack and priority[elem] <= priority[stack[-1]]