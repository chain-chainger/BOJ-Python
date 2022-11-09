def solve(index):
	global res
	if index == len(s):
		res = 1
		return
	if check[index] == 1:
		return
	check[index] = 1
	for i in range(len(a)):
		if len(s[index:]) >= len(a[i]):
			if s[index:index + len(a[i])] == a[i]:
				solve(index + len(a[i]))

s = input()
a = []
n = int(input())
for _ in range(n):
	a.append(input())
check = [0] * 100
res = 0
solve(0)
print(res)
