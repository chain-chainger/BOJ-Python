import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
possible = a // 2 + b
if possible > n:
    print(n)
else:
    print(possible)