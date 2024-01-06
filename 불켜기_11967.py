import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	visited = [[-1] * (N + 1) for _ in range(N + 1)]
	visited[1][1] = 1
	queue = deque([(1, 1, rooms[1][1])])
	answer = 1

	while queue:
		r, c, switches = queue.popleft()
		for a, b in switches:
			if visited[a][b] == -1:
				visited[a][b] = 0
				answer += 1
				for i in range(4):
					nr = a + dr[i]
					nc = b + dc[i]
					if nr < 1 or nr > N or nc < 1 or nc > N:
						continue
					if visited[nr][nc] == 1:
						queue.append((a, b, rooms[a][b]))
						visited[a][b] = 1

		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 1 or nr > N or nc < 1 or nc > N:
				continue
			if visited[nr][nc] == 0:
				queue.append((nr, nc, rooms[nr][nc]))
				visited[nr][nc] = 1
	
	return answer

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
rooms = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
info = [list(map(int, input().split())) for _ in range(M)]

for line in info:
	x, y, a, b = line
	rooms[x][y].append((a, b))

print(bfs())
