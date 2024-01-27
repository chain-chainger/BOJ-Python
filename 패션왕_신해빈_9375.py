import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	clothes = {}

	for _ in range(n):
		name, type = input().rstrip().split()

		if type in clothes:
			clothes[type].append(name)
		else:
			clothes[type] = [name]

	answer = 1
	for type in clothes:
		answer *= len(clothes[type]) + 1

	print(answer - 1)
