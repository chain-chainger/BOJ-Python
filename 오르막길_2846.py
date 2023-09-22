import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
count = 0
answer = []
for i in range(1, n):
    if sequence[i] > sequence[i - 1]:
        count += sequence[i] - sequence[i - 1]
        if i == n - 1:
           answer.append(count)
    else:
        answer.append(count)
        count = 0
print(max(answer))