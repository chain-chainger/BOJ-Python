import sys
input = sys.stdin.readline

K = int(input())
answer = []
for _ in range(K):
	number = int(input())
	if number == 0:
		answer.pop()
	else:
		answer.append(number)
print(sum(answer))
