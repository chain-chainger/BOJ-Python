import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue, next_queue):
	count = 0
	while queue:
		r, c, castle, distance = queue.popleft()
		if distance == 0:
			next_queue.append([r, c, castle, distances[castle - 1]])
			continue
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= N or nc < 0 or nc >= M:
				continue
			if board[nr][nc] == '.' and visited[nr][nc] == 0:
				visited[nr][nc] = castle
				queue.append([nr, nc, castle, distance - 1])
				count += 1
	return count

def solve():
	queues = [deque() for _ in range(P)]
	temp_queue = deque()

	for i in range(N):
		for j in range(M):
			if board[i][j].isdigit():
				castle = int(board[i][j])
				visited[i][j] = castle
				queues[castle - 1].append([i, j, castle, distances[castle - 1]])

	while True:
		count = 0
		for i in range(P):
			count += bfs(queues[i], temp_queue)
			queues[i] = temp_queue.copy()
			temp_queue.clear()
		if count == 0:
			break

	for castle in range(1, P + 1):
		castle_count = 0
		for i in range(N):
			castle_count += visited[i].count(castle)
		print(castle_count, end=' ')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, P = map(int, input().split())
distances = list(map(int, input().split()))
board = [input().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

solve()
