import sys
input = sys.stdin.readline
def main():
    string = input().rstrip()
    char_dict = {}
    character = "abcdefghijklmnopqrstuvwxyz"
    for elem in character:
        char_dict[elem] = 0
    for elem in string:
        char_dict[elem] += 1
    print(*char_dict.values())
    return

main()