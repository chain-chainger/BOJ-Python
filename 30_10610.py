n = list(input())
n.sort(reverse=True)
check = 0
for num in n:
    check = int(num)
if check % 3 != 0 or n[-1] != '0':
    print(-1)
else:
    print(''.join(n))