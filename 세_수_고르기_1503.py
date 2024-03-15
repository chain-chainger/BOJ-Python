import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
answer = sys.maxsize

for x in range(1, 1002):
	if x in s:
		continue
	for y in range(1, 1002):
		if y in s:
			continue
		for z in range(1, 1002):
			if z in s:
				continue
			xyz = x * y * z
			if abs(n - xyz) < answer:
				answer = abs(n - xyz)
			if n + 1 < xyz:
				break
print(answer)
