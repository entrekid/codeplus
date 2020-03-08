import sys
input = sys.stdin.readline

def concern(string):
    cnt = 0
    for elem in string:
        if elem == "(":
            cnt += 1
        else:
            if cnt:
                cnt -= 1
            else:
                return "NO"
    if cnt:
        return "NO"
    else:
        return "YES"

def main():
    test_case = int(input())
    for _ in range(test_case):
        print(concern(input().rstrip()))

main()