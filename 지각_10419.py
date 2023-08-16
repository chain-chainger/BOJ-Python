import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 1
    while answer + (answer ** 2) <= n:
        answer += 1
    print(answer - 1)
