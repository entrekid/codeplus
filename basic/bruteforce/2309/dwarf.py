import sys
input = sys.stdin.readline
dwarf_list = [int(input()) for _ in range(9)]
dwarf_list.sort()
left = sum(dwarf_list) - 100
for iter in range(9):
    for jter in range(iter + 1, 9):
        if dwarf_list[iter] + dwarf_list[jter] == left:
            for kter in range(9):
                if kter != iter and kter != jter:
                    print(dwarf_list[kter])
            exit()


