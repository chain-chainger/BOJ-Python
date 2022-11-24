s = input()
k = input()
res = []
for c in s:
	if (ord(c) >= 63 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
		res.append(c)
if k in ''.join(res):
	print(1)
else:
	print(0)
