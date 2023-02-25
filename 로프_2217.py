import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
max_weight = 0
ropes.sort()
for i in range(n):
    temp = ropes[i] * (n - i)
    if temp > max_weight:
        max_weight = temp
print(max_weight)
