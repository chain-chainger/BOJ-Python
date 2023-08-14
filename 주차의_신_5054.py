import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stores = sorted(map(int, input().split()))
    print((stores[-1] - stores[0]) * 2)