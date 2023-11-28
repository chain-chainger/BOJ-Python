import sys
input = sys.stdin.readline

answer = []
for _ in range(10):
	number = int(input())
	answer.append(number % 42)
print(len(set(answer)))
