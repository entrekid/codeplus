import sys
n = 9
dwarf_list = [int(input()) for _ in range(n)]
dwarf_list.sort()
total = sum(dwarf_list)
for iter in range(n):
    for jter in range(iter + 1, n):
        if total - (dwarf_list[iter] + dwarf_list[jter]) == 100:
            for kter in range(n):
                if kter == iter or kter == jter:
                    continue
                print(dwarf_list[kter])
            sys.exit(0)