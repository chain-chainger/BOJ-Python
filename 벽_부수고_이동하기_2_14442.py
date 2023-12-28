import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
	queue = deque()
	queue.append([0, 0, K])
	visited[0][0][K] = 1

	while queue:
		r, c, count = queue.popleft()

		if r == N - 1 and c == M - 1:
			print(visited[r][c][count])
			return
			
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >= N or nc < 0 or nc >= M:
				continue
			if board[nr][nc] == '1' and count > 0 and  visited[nr][nc][count - 1] == 0:
				queue.append([nr, nc, count - 1])
				visited[nr][nc][count - 1] = visited[r][c][count] + 1
			elif board[nr][nc] == '0' and visited[nr][nc][count] == 0:
				queue.append([nr, nc, count])
				visited[nr][nc][count] = visited[r][c][count] + 1
	print(-1)	

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
bfs()
