import sys
input = sys.stdin.readline

N = int(input())
numbers = input().rstrip()
answer = 0

for i in range(N):
    answer += int(numbers[i])

print(answer)