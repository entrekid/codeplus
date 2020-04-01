import sys
input = sys.stdin.readline
dwarf_list = [int(input()) for _ in range(9)]
dwarf_list.sort()
done = False
left = sum(dwarf_list) - 100
for iter in range(9):
    if iter + 1 < 9 and done == False:
        for jter in range(iter + 1, 9):
            if dwarf_list[iter] + dwarf_list[jter] == left:
                tgt1, tgt2 = dwarf_list[iter], dwarf_list[jter]
                dwarf_list.remove(tgt1)
                dwarf_list.remove(tgt2)
                done = True
                break
        
for elem in dwarf_list:
    print(elem)
