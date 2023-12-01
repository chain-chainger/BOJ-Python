import sys
input = sys.stdin.readline

def solve():
	for i in range(1, N + 1):
		weight = objects[i][0] 
		value = objects[i][1]
		for j in range(1, K + 1):
			if j < weight:
				backpack[i][j] = backpack[i - 1][j]
			else:
				backpack[i][j] = max(value + backpack[i - 1][j - weight], backpack[i - 1][j])
	return backpack[N][K]

N, K = map(int, input().split())
objects = [[0, 0]]
backpack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
	objects.append(list(map(int, input().split())))

print(solve())
