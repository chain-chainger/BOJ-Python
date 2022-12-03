count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    n = n * 3
    if n % 2 == 0:
        flag = True
        n = n // 2
    else:
        flag = False
        n = (n + 1) // 2
    n = n * 3 // 9
    if flag:
        n * 2
        print(f"{count}. even {n}")
    else:
        n * 2 + 1
        print(f"{count}. odd {n}")
