import sys
input = sys.stdin.readline
def main():
    n, b = map(int, input().rstrip().split())
    char_dict = {}
    character = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for iter in range(36):
        char_dict[iter] = character[iter]
    ans = ""
    if not n:
        ans += '0'
    while n:
        ans = char_dict[n % b] + ans
        n = n // b
    print(ans)
    return
main()
    