from collections import deque
import sys
input = sys.stdin.readline

def bfs():
	queue = deque([s])
	while queue:
		visited[s] = 1
		index = queue.popleft()
		if index == g:
			break
		if index + u <= f and visited[index + u] == 0:
			visited[index + u] = visited[index] + 1
			queue.append(index + u)
		if index - d > 0 and visited[index - d] == 0:
			visited[index - d] = visited[index] + 1
			queue.append(index - d)


f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
bfs()
if visited[g] == 0:
	print("use the stairs")
else:
	print(visited[g] - 1)
