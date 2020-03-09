import sys
input = sys.stdin.readline

check = [False] * 1001

def main():
    test_case = int(input())
    num_list = list(map(int, input().rstrip().split()))
    check[1] = True
    for iter in range(2, 1001):
        if not check[iter]:
            for jter in range(iter + iter, 1001, iter):
                check[jter] = True
    cnt = 0
    for elem in num_list:
        if check[elem] == False:
            cnt += 1
    print(cnt)
    return
main()