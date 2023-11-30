from collections import deque
import sys
input = sys.stdin.readline

def BFS():
	while f_queue:
		r, c = f_queue.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= R or nc < 0 or nc >= C:
				continue
			if f_visited[nr][nc] or maze[nr][nc] == '#':
				continue
			f_visited[nr][nc] = f_visited[r][c] + 1
			f_queue.append((nr, nc))
	while j_queue:
		r, c = j_queue.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= R or nc < 0 or nc >= C:
				return j_visited[r][c] + 1
			if j_visited[nr][nc] or maze[nr][nc] == '#' or maze[nr][nc] == 'F':
				continue
			if f_visited[nr][nc] == 0 or f_visited[nr][nc] > j_visited[r][c] + 1:
				j_visited[nr][nc] = j_visited[r][c] + 1
				j_queue.append((nr, nc))
	return("IMPOSSIBLE")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
j_queue, f_queue = deque(), deque()
j_visited, f_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
maze = []
for i in range(R):
	maze.append(list(input().rstrip()))
	for j in range(C):
		if maze[i][j] == 'J':
			if i == 0 or i == R or j == 0 or j == C:
				print(1)
				exit()
			j_queue.append((i, j))
		elif maze[i][j] == 'F':
			f_queue.append((i, j))
print(BFS())
