while True:
	s = input()
	if s == '#':
		break
	alphabet = s[0]
	s = s.lower()
	cnt = 0
	for i in range(1, len(s)):
		if alphabet == s[i]:
			cnt += 1
	print(alphabet, cnt)
