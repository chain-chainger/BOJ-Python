import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    for k in range(1, n):
        if k ** 2 <= n:
            answer += 1
        if k ** 2 > n:
            break
    print(answer)