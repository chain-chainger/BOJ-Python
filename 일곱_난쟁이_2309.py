dwarfs = []
sum = 0
for i in range(9):
    dwarfs.append(int(input()))
    sum += dwarfs[i]
flag = False
for i in range(8):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == sum - 100:
            save = [i, j]
            flag = True
            break
        if flag:
            break
del dwarfs[save[0]]
del dwarfs[save[1] - 1]
dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)