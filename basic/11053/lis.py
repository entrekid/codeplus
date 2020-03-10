"""
10 20 10 30 20 50
1   
"""
def main():
    num = int(input())
    num_list = list(map(int, input().split()))
    dp_list = [1] * num
    no_max = dp_list[0]
    for iter in range(num):
        for jter in range(iter):
            if num_list[iter] > num_list[jter]:
                dp_list[iter] = max(dp_list[iter], dp_list[jter] + 1)
        no_max = max(no_max, dp_list[iter])
    print(no_max)
    return
main()