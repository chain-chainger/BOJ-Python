import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
	queue = deque()
	queue.append((row, col))
	visited[row][col] = 1
	count = 0

	while queue:
		r, c = queue.popleft()

		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]

			if nr < 0 or nr >= n or nc < 0 or nc >= m:
				continue
			if visited[nr][nc] == 0 and campus[nr][nc] != 'X':
				queue.append((nr, nc))
				visited[nr][nc] = 1
				if campus[nr][nc] == 'P':
					count += 1

	if count:
		return count
	else:
		return 'TT'

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
campus = [input().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
	for j in range(m):
		if campus[i][j] == 'I':
			print(bfs(i, j))
