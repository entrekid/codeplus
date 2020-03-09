import sys
print = sys.stdout.write
input = sys.stdin.readline

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    num = int(input())
    print(str(factorial(num)))
    print("\n")
    return
main()