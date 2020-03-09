import sys
input = sys.stdin.readline
def main():
    word = input().rstrip()
    stack = []
    tag = False
    ans = ""
    for elem in word:
        if elem == "<":
            tag = True
            while stack:
                ans += stack.pop()
            ans += elem
        elif elem == ">":
            ans += ">"
            tag = False
        elif tag:
            ans += elem
        # tag 안에 있는 문자열 모두 정리
        else:
            if elem == " ":
                while stack:
                    ans += stack.pop()
                ans += elem
            else:
                stack.append(elem)
    while stack:
        ans += stack.pop()
    print(ans)
    return
main()
