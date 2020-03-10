import sys
input = sys.stdin.readline

check = [False] * 1000001
check[0] = True
check[1] = True
for iter in range(2, 1000001):
    if not check[iter]:
        for jter in range(iter + iter, 1000001, iter):
            check[jter] = True

def goldbach(num):
    cnt = 0
    for iter in range(3, num // 2 + 1):
        if not check[iter] and not check[num - iter]:
            cnt += 1
    return cnt

def main():
    test_case = int(input())
    for _ in range(test_case):
        print(goldbach(int(input())))

main()