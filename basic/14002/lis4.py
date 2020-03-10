def go(num_list, check, no_max):
    if no_max == check[no_max]:
        print(num_list[no_max], end = " ")
        return
    else:
        go(num_list, check, check[no_max])
        print(num_list[no_max], end = " ")
        return
    return


def main():
    num = int(input())
    num_list = list(map(int, input().split()))
    dp_list = [1] * num
    check = [0] * num
    no_max = 0
    max_idx = 0
    for iter in range(num):
        check[iter] = iter
        for jter in range(iter):
            if num_list[iter] > num_list[jter]:
                basis = dp_list[iter]
                dp_list[iter] = max(dp_list[iter], dp_list[jter] + 1)
                if basis != dp_list[iter]:
                    check[iter] = jter
        basis_max = no_max
        no_max = max(no_max, dp_list[iter])
        if no_max != basis_max:
            max_idx = iter
    print(no_max)
    # 경로 순회
    go(num_list, check, max_idx)
    print()
    return
main()
