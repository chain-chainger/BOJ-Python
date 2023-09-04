import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0
for i in range(n):
	find = numbers[:i] + numbers[i + 1:]
	left = 0
	right = n - 2
	while True:
		temp = find[left] + find[right]
		if temp == numbers[i]:
			answer += 1
			break
		if temp > numbers[i]:
			right -= 1
		else:
			left += 1
		if left >= right:
			break
print(answer)
