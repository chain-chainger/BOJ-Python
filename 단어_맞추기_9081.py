def solve():
	check = -1
	for i in range(len(s) - 1):
		if s[i] < s[i + 1]:
			check = i
	if check == -1:
		print(''.join(s))
		return
	for i in range(len(s) - 1, -1, -1):
		if s[check] < s[i]:
			s[check], s[i] = s[i], s[check]
			s[check+1:] = reversed(s[check+1:])
			print(''.join(s))
			return

t = int(input())
for _ in range(t):
	s = list(input())
	solve()
