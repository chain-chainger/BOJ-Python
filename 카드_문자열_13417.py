t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(str, input().split()))
	res = [arr[0]]
	for i in range(1, n):
		if arr[i] <= res[0]:
			res.insert(0, arr[i])
		else:
			res.append(arr[i])
	print(''.join(res))
