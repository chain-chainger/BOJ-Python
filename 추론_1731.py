import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
answer = sequence[-1]
if sequence[2] - sequence[1] == sequence[1] - sequence[0]:
    answer += (sequence[1]-sequence[0])
elif sequence[2] // sequence[1] == sequence[1] // sequence[0]:
    answer *= (sequence[1] // sequence[0])
print(answer)
