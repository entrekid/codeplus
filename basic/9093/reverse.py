import sys
input = sys.stdin.readline

def translate(string):
    stack = []
    ans = ""
    string = string + " "
    for elem in string:
        if elem == " ":
            while stack:
                ans += stack.pop()
            ans += elem
        else:
            stack.append(elem)
    return ans

def main():
    test_case = int(input())
    for _ in range(test_case):
        print(translate(input().rstrip()))
    
main()