import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
	queue = deque()
	queue.append([0, 0, K, 1])
	visited[0][0][K] = 1

	while queue:
		r, c, left, time = queue.popleft()

		if r == N - 1 and c == M - 1:
			print(visited[r][c][left])
			return
			
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= N or nc < 0 or nc >= M:
				continue
			if board[nr][nc] == '0' and visited[nr][nc][left] == 0:
				queue.append([nr, nc, left,  time + 1])
				visited[nr][nc][left] = time + 1
			elif board[nr][nc] == '1' and left > 0 and visited[nr][nc][left - 1] == 0:
				if time % 2 == 1:
					queue.append([nr, nc, left - 1,  time + 1])
					visited[nr][nc][left - 1] = time + 1
				else:
					queue.append([r, c, left, time + 1])
	print(-1)	

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
bfs()
