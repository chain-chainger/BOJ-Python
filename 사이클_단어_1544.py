n = int(input())
words = []
cnt = 0
for i in range(n):
	s = input()
	flag = True
	for word in words:
		temp = word
		for j in range(len(temp)):
			if temp == s:
				flag = False
				break
			temp = temp[1:] + temp[0]
	if flag:
		cnt += 1
	words.append(s)
print(cnt)
