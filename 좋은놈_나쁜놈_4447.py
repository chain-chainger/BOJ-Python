import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    name = input().rstrip()
    g_count = name.count('g') + name.count('G')
    b_count = name.count('b') + name.count('B')
    if g_count > b_count:
        print(f"{name} is GOOD")
    elif g_count < b_count:
        print(f"{name} is A BADDY")
    else:
        print(f"{name} is NEUTRAL")