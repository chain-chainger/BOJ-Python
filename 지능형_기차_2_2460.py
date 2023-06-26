import sys
input = sys.stdin.readline

current = 0
answer = 0
for _ in range(10):
    subtract, add = map(int, input().split())
    current -= subtract
    current += add
    if current > answer:
        answer = current
print(answer)