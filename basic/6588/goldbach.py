import sys
input = sys.stdin.readline

# 에라토스테네스의 체
check = [False] * 1000001
check[0] = True
check[1] = True
for iter in range(2, 1000001):
    if not check[iter]:
        for jter in range(iter + iter, 1000001, iter):
            check[jter] = True

def main():
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            for iter in range(3, num // 2 + 1):
                if not check[iter] and not check[num - iter]:
                    print(num, "=", iter, "+", num - iter)
                    break
                else:
                    continue
            else:
                print("Goldbach's conjecture is wrong.")
    return
main()