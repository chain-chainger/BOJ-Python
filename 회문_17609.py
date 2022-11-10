def solve(left, right, cnt):
	while left < right:
		if s[left] == s[right]:
			left += 1
			right -= 1
		elif cnt == 0:
			check = 0
			check += solve(left + 1, right, 1)
			check += solve(left, right - 1, 1)
			return check // 2
		else:
			return 2
	return 0

t = int(input())
for _ in range(t):
	s = input()
	print(solve(0, len(s) - 1, 0))
