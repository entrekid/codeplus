div = 10007
dp_list = [0] * 1001
dp_list[1] = 1
dp_list[2] = 2
def main():
    num = int(input())
    for iter in range(3, num + 1):
        dp_list[iter] = (dp_list[iter - 1] + dp_list[iter - 2]) % div
    print(dp_list[num])
    return
main()