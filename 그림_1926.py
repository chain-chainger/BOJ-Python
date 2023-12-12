import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
	count = 0
	queue = deque([(row, col)])
	visited[row][col] = 1
	while(queue):
		r, c = queue.popleft()
		count += 1
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= n or nc < 0 or nc >= m:
				continue
			if board[nr][nc] == 1 and visited[nr][nc] == 0:
				queue.append([nr, nc])
				visited[nr][nc] = 1
	area.append(count)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
count = 0
area = []

for i in range(n):
	for j in range(m):
		if board[i][j] == 1 and visited[i][j] == 0:
			bfs(i, j)
			count += 1

if count == 0:
	print(0, 0)
else:
	print(f"{count}\n{max(area)}")
