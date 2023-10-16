import sys
input = sys.stdin.readline

n = int(input())
class_info = [list(map(int, input().split())) for _ in range(n)]
counts = [0] * n
check = [[False] * n for _ in range(n)]
for grade in range(5):
	for i in range(n -1):
		for j in range(i + 1, n):
			if class_info[i][grade] == class_info[j][grade] and check[i][j] == False:
				counts[i] += 1
				check[i][j] = True
				counts[j] += 1
				check[j][i] = True
print(counts.index(max(counts)) + 1)
