n = int(input())
words = [input() for _ in range(n)]
words.sort(key=len)
cnt = 0
for i in range(n):
	for j in range(i + 1, n):
		if words[i] == words[j][:len(words[i])]:
			cnt += 1
			break
print(n - cnt)
