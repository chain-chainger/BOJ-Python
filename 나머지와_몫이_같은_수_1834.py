import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1, n):
    answer += n * i + i
print(answer)