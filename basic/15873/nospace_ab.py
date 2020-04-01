string = input()
length = len(string)
if length == 2:
    print(int(string[0]) + int(string[1]))
else:
    zero = string.count("0")
    if zero == 1:
        idx = string.index("0")
        if idx == 2:
            print(10 + int(string[0]))
        else:
            print(10 + int(string[2]))
    elif zero == 2:
        print(20)
