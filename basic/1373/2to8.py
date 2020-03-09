import sys
input = sys.stdin.readline
from collections import deque
def convert(string):
    ret = 0
    for elem in string:
        ret *= 2
        ret += int(elem)
    return str(ret)
        
def main():
    string = deque(input().rstrip())
    ans = ""
    length = len(string)
    while length % 3 != 0:
        string.appendleft("0")
        length += 1
    while string:
        num = []
        for _ in range(3):
            num.append(string.popleft())
        ans += convert(num)
    print(ans)
    return
main()
