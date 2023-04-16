from collections import deque
import sys
input = sys.stdin.readline

def bfs():
	queue = deque([(0, 0)])
	melt = []
	visited[0][0] = 1
	while queue:
		r, c = queue.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nc < 0 or nr >= height or nc >= width:
				continue
			if visited[nr][nc] == 0:
				visited[nr][nc] = 1
				if matrix[nr][nc] == 1:	
					melt.append((nr, nc))
				else:
					queue.append((nr, nc))
	for r, c in melt:
		matrix[r][c] = 0
	return len(melt)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
height, width = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(height)]
prev_count = 0
time_count = 0
while True:
	visited = [[0] * width for _ in range(height)]
	count = bfs()
	if count == 0:
		print(time_count, prev_count, sep='\n')
		break
	prev_count = count
	time_count += 1
