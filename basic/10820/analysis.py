import sys
# input = sys.stdin.readline

def main():
    while True:
        number = "0123456789"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        num_blank = 0
        num_upper = 0
        num_lower = 0
        num_number = 0
        try:
            word = input()
        except:
            exit()
        for elem in word:
            if elem == " ":
                num_blank += 1
            elif elem in number:
                num_number += 1
            elif elem in upper:
                num_upper += 1
            elif elem in lower:
                num_lower += 1
        print(num_lower, num_upper, num_number, num_blank)
    return
main()
        