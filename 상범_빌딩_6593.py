import sys
from collections import deque
input = sys.stdin.readline

def bfs(layer, row, col):
	queue = deque()
	queue.append((layer, row, col))
	visited[layer][row][col] = 1

	while queue:
		l, r, c = queue.popleft()
		for i in range(6):
			nl = l + dl[i]
			nr = r + dr[i]
			nc = c + dc[i]
			if nl < 0 or nl >= L or nr < 0 or nr >= R or nc < 0 or nc >= C:
				continue
			if building[nl][nr][nc] == 'E':
				print(f"Escaped in {visited[l][r][c]} minute(s).")
				return
			elif building[nl][nr][nc] == '.' and visited[nl][nr][nc] == 0:
				queue.append((nl, nr, nc))
				visited[nl][nr][nc] = visited[l][r][c] + 1
	
	print("Trapped!")


dl = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

while True:
	L, R, C = map(int, input().split())
	if L == R == C == 0:
		break
	building = []
	for _ in range(L):
		temp = [input().rstrip() for _ in range(R)]
		building.append(temp)
		temp = input()
	visited = [[[0] * C for _ in range(R)] for _ in range(L)]
	for i in range(L):
		for j in range(R):
			for k in range(C):
				if building[i][j][k] == 'S':
					bfs(i, j, k)

