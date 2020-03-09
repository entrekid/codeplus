import sys
input = sys.stdin.readline

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_dict = {}
    for elem in alphabet:
        char_dict[elem] = -1
    word = input().rstrip()
    for elem in word:
        char_dict[elem] = word.index(elem)
    print(*char_dict.values())
    return

main()