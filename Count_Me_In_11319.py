vowels = "aeiouAEIOU"
s = int(input())
for _ in range(s):
	line = input()
	cnt_vowel = 0
	cnt_alpha = 0
	for c in line:
		if c in vowels:
			cnt_vowel += 1
		elif c.isalpha():
			cnt_alpha += 1
	print(cnt_alpha, cnt_vowel)
