vowels = "aeiou"
s = input()
cnt = 0
for c in s:
	if c in vowels:
		cnt += 1
print(cnt)
