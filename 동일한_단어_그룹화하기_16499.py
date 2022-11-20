n = int(input())
groups = set()
for _ in range(n):
	groups.add(''.join(sorted(input())))
print(len(groups))
