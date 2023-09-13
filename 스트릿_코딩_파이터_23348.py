import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
n = int(input())
answer = 0
for _ in range(n):
    sum = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        sum += (A * a) + (B * b) + (C * c)
    if sum > answer:
        answer = sum
print(answer)