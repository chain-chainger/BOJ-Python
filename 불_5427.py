import sys
from collections import deque
input = sys.stdin.readline

def solve():
	w, h = map(int, input().split())
	board = [input().rstrip() for _ in range(h)]
	fire_info = [[0] * w for _ in range(h)]
	visited = [[0] * w for _ in range(h)]

	row, col = 0, 0
	queue = deque()

	for i in range(h):
		for j in range(w):
			if board[i][j] == '@':
				row = i
				col = j
			elif board[i][j] == '*':
				queue.append((i, j))
				visited[i][j] = 1
				fire_info[i][j] = 1
	while queue:
		r, c = 	queue.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= h or nc < 0 or nc >= w:
				continue
			if board[nr][nc] != '#' and visited[nr][nc] == 0:
				queue.append((nr, nc))
				visited[nr][nc] = 1
				fire_info[nr][nc] = fire_info[r][c] + 1
	
	visited = [[0] * w for _ in range(h)]
	queue.append((row, col))
	visited[row][col] = 1

	while queue:
		r, c = queue.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= h or nc < 0 or nc >= w:
				return visited[r][c]
			if board[nr][nc] != '#' and visited[nr][nc] == 0:
				if visited[r][c] + 1 < fire_info[nr][nc] or fire_info[nr][nc] == 0:
					queue.append((nr, nc))
					visited[nr][nc] = visited[r][c] + 1
	return "IMPOSSIBLE"

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
t = int(input())
for _ in range(t):
	print(solve())
