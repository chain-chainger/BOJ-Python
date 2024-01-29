import sys
from collections import deque
input = sys.stdin.readline

def bfs(target_row):
	visited = [0] * n
	queue = deque()
	queue.append(target_row)

	while queue:
		row = queue.popleft()

		for col in range(n):
			if visited[col] == 0 and graph[row][col] == 1:
				answer[target_row][col] = 1
				visited[col] = 1
				queue.append(col)
	


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for i in range(n):
	bfs(i)

for line in answer:
	print(*line)
