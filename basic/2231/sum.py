def change(num):
    ret = num
    for elem in str(num):
        ret += int(elem)
    return ret
 
MAX = 1000000
# max까지 쭈욱 생성자로 숫자 만들고
# 역으로 거슬러 올라감
num_list = [0] * 1000001
for iter in range(MAX + 1):
    if num_list[iter] == 0:
        if change(iter) <= MAX:
            num_list[change(iter)] = iter
    else:
        if change(iter) <= MAX and num_list[change(iter)] == 0:
            num_list[change(iter)] = iter

basis = int(input())
print(num_list[basis])