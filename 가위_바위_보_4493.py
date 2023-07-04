import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p1, p2 = 0, 0
    n = int(input())
    for i in range(n):
        a, b = input().rstrip().split()
        if a == b:
            continue
        elif (a == 'R' and b == 'S') or (a == 'P' and b == 'R') or (a == 'S' and b == 'P'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")