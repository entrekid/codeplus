import sys
input = sys.stdin.readline

def main():
    num = int(input())
    no_5 = 0
    while num:
        no_5 += num // 5
        num = num // 5
    print(no_5)
    return

main()