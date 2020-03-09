import sys
input = sys.stdin.readline
def main():
    a, b, c, d = input().rstrip().split()
    x = a + b
    y = c + d
    ans = int(x) + int(y)
    print(ans)
    return

main()
