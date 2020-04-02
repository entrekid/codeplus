def palindrome(num):
    length = len(num)
    if length % 2 and length > 1:
        if num[0] == num[-1]:
            return palindrome(num[1:-1])
        else:
            return 0
    elif length == 1 or length == 0:
        return 1
    else:
        if num[0] == num[-1]:
            return palindrome(num[1:-1])
        else:
            return 0
while True:
    num = input()
    if num == "0":
        break
    if palindrome(num):
        print("yes")
    else:
        print("no")