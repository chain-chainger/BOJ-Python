import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(a, b):
	x, y = a, b
	visited[x][y] = 1
	count = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if map[nx][ny] < 1:
			count += 1
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if map[nx][ny] > 0 and visited[nx][ny] == 0:
			visited[nx][ny] = 1
			dfs(nx, ny)
	map[x][y] -= count

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]
year = 0
while True:
	visited = [[0] * m for _ in range(n)]
	count = 0
	for i in range(n):
		for j in range(m):
			if map[i][j] > 0 and visited[i][j] == 0:
				count += 1
				dfs(i, j)
	if count == 0:
		print(0)
		break
	elif count >= 2:
		print(year)
		break
	year += 1
