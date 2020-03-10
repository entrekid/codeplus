import sys
input = sys.stdin.readline
print = sys.stdout.write
check = [False] * 10000001
check[0] = True
check[1] = True
prime_list = []
def main():
    num = int(input())
    idx = 0
    size = 0
    for iter in range(2, num + 1):
        if not check[iter]:
            prime_list.append(iter)
            size += 1
            for jter in range(iter + iter, num + 1, iter):
                check[jter] = True
    while num and idx < size:
        if num % prime_list[idx] == 0:
            num = num // prime_list[idx]
            print(str(prime_list[idx]))
            print("\n")
        else:
            idx += 1
    return
main()