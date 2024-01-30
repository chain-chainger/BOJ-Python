import sys
input = sys.stdin.readline

def dfs(row, col, sum, len):
	global answer

	if len == 4:
		if sum > answer:
			answer = sum
	else:
		for i in range(4):
			nr = row + dr[i]
			nc = col + dc[i]
			if nr < 0 or nr >= n or nc < 0 or nc >= m:
				continue
			if visited[nr][nc] == 0:
				visited[nr][nc] = 1
				dfs(nr, nc, sum + board[nr][nc], len + 1)
				visited[nr][nc] = 0

def edge_check(row, col):
	global answer

	for i in range(4):
		poliomino = board[row][col]
		for j in range(3):
			nr = row + dr[(i + j) % 4]
			nc = col + dc[(i + j) % 4]
			if nr < 0 or nr >= n or nc < 0 or nc >= m:
				poliomino = 0
				break
			poliomino += board[nr][nc]
		if poliomino > answer:
			answer = poliomino

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
	for j in range(m):
		visited[i][j] = 1
		dfs(i, j, board[i][j], 1)
		visited[i][j] = 0
		edge_check(i, j)

print(answer)
