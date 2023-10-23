import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    position = 0
    while n > 0:
        if n % 2 == 1:
            print(position, end=' ')
        n = n // 2
        position += 1
        