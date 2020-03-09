"""
A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z
"""
import sys
input = sys.stdin.readline

def main():
    word = input().rstrip()
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper_dict = {}
    lower_dict = {}
    for iter in range(26):
        if iter <= 12:
            upper_dict[upper[iter]] = upper[iter + 13]
            lower_dict[lower[iter]] = lower[iter + 13]
        else:
            upper_dict[upper[iter]] = upper[iter - 13]
            lower_dict[lower[iter]] = lower[iter - 13]
    ans = ""
    for elem in word:
        if elem.isupper():
            ans += upper_dict[elem]
        elif elem.islower():
            ans += lower_dict[elem]
        else:
            ans += elem
    print(ans)
    return
main()

