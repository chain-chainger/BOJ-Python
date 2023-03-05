from collections import deque
import sys
input = sys.stdin.readline

def bfs():
	dz = [1, -1, 0, 0, 0, 0]
	dy = [0, 0, 1, -1, 0, 0]
	dx = [0, 0, 0, 0, 1, -1]
	while(queue):
		z, y, x = queue.popleft()
		for i in range(6):
			nz = z + dz[i]
			ny = y + dy[i]
			nx = x + dx[i]
			if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and graph[nz][ny][nx] == 0:
				queue.append([nz, ny, nx])
				graph[nz][ny][nx] = graph[z][y][x] + 1

m, n, h = map(int, input().split())
graph = []
queue = deque([])
for i in range(h):
	temp = []
	for j in range(n):
		temp.append(list(map(int, sys.stdin.readline().split())))
		for k in range(m):
			if temp[j][k] == 1:
				queue.append([i, j, k])
	graph.append(temp)
bfs()
count = 0
for i in graph:
	for j in i:
		for k in j:
			if k == 0:
				print(-1)
				exit(0)
		count = max(count, max(j))
print(count - 1)
