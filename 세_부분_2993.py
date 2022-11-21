s = input()
len_s = len(s)
s_arr = []
for i in range(1, len_s - 1):
	for j in range(1, len_s - 1):
		if i + j <= len_s - 1:
			s_arr.append(s[:i][::-1] + s[i:i + j][::-1] + s[i + j:][::-1])
print(sorted(s_arr)[0])
