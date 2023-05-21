import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))
count = 0
for coin in reversed(coins):
    count += k // coin
    k = k % coin
print(count)