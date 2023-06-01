import sys
input = sys.stdin.readline

m, n = map(int, input().split())
for number in range (m, n + 1):
	if number == 1:
		continue
	for j in range(2, int(number ** 0.5) + 1):
		if number % j==0:
			break
	else:
		print(number)
