def main():
    num = int(input())
    ans = ""
    while num:
        if num % (-2):
            ans = '1' + ans
            num = num // -2 + 1
        else:
            ans = "0" + ans
            num = num // -2
    if not ans:
        print("0")
    else:
        print(ans)
    return
main()
