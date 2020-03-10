num = int(input())
sqr = int(num ** 0.5)
power_list = [elem ** 2 for elem in range(1, sqr + 1)]
dp_list = [0] * (num + 1)
dp_list[1] = 1
if num >= 2:
    dp_list[2] = 2
    for elem in power_list:
        dp_list[elem] = 1
    for iter in range(3, num + 1):
        if dp_list[iter]:
            continue
        possible_list = []
        for elem in power_list:
            if iter >= elem:
                possible_list.append(dp_list[elem] + dp_list[iter - elem])
        dp_list[iter] = min(possible_list)

print(dp_list[num])