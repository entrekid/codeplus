import sys
input = sys.stdin.readline
check = [False] * 1000001
def main():
    a, b = map(int, input().rstrip().split())
    check[1] = True
    for iter in range(2, 1000001):
        if not check[iter]:
            for jter in range(iter + iter, 1000001, iter):
                check[jter] = True
    for kter in range(a, b + 1):
        if check[kter]:
            continue
        else:
            print(kter)
    return
main()