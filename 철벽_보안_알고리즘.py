t = int(input())
for _ in range(t):
    n = int(input())
    key_1 = input().split()
    key_2 = input().split()
    solve = []
    for s in key_1:
        solve.append(key_2.index(s))
    cipher = input().split()
    res = []
    for i in solve:
        res.append(cipher[i])
    print(' '.join(res))