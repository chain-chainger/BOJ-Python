s = input()
ucpc = "UCPC"
i = 0
flag = False
for c in s:
    if c == ucpc[i]:
        i += 1
    if i == 4:
        flag = True
        break
if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")