import sys
input = sys.stdin.readline
def main():
    n, b = input().rstrip().split()
    character = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_dict = {}
    for iter in range(36):
        char_dict[character[iter]] = iter
    ret = 0
    for elem in n:
        ret *= int(b)
        ret += int(char_dict[elem])
    print(ret)
    return
main()