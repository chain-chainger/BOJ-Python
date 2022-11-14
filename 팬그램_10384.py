n = int(input())
for _ in range(n):
	s = input().lower()
	alpha = [0] * 26
	for c in s:
		if ord(c) >= 97 and ord(c) <= 123:
			alpha[ord(c)-97] += 1
	if min(alpha) >= 3:
		print(f"Case {_ + 1}: Triple pangram!!!")
	elif min(alpha) == 2:
		print(f"Case {_ + 1}: Double pangram!!")
	elif min(alpha) == 1:
		print(f"Case {_ + 1}: Pangram!")
	else:
		print(f"Case {_ + 1}: Not a pangram")

