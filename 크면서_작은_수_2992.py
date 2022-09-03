import math
x = input()
value = sorted(x)
r_max = int(math.pow(10, len(x)))
check = True
for i in range(int(x), r_max):
    if value == sorted(str(i)):
        if i > int(x):
            print(i)
            check = False
            break
if check:
    print(0)
