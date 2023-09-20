import sys
input = sys.stdin.readline

for _ in range(3):
	number = input().rstrip()
	max = 1
	count = 1
	for i in range(1, 8):
		if number[i] == number[i - 1]:
			count += 1
		else:
			count = 1
		if count > max:
			max = count
	print(max)
