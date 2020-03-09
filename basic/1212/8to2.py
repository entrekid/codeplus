import sys
input = sys.stdin.readline

def convert(string):
    num = int(string)
    ans = ""
    while num:
        ans = str(num % 2) + ans
        num = num // 2
    length = len(ans)
    while length % 3 != 0:
        ans = "0" + ans
        length += 1
    if length == 0:
        ans = "000"
    return ans

def main():
    num = input().rstrip()
    ans = ""
    for elem in num:
        ans += convert(elem)
    while ans and ans[0] == "0":
        ans = ans[1:]
    if not ans:
        ans = "0"
    print(ans)
    return

main()
