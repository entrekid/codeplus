import sys
input = sys.stdin.readline

def main():
    word = input().rstrip()
    suffix_list = []
    length = len(word)
    for iter in range(length):
        suffix_list.append(word[iter:])
    suffix_list.sort()
    print(*suffix_list, sep = "\n")
    return
main()