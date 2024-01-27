import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target):
	visited = [0] * 10000
	queue = deque()
	queue.append((start, ''))
	visited[start] = 1

	while queue:
		current, answer = queue.popleft()
		
		if current == target:
			return answer
		
		d = current * 2 % 10000
		s = (current - 1) if current > 0 else 9999
		l = (current // 1000) + current * 10 % 10000
		r = (current % 10 * 1000) + current // 10

		if visited[d] == 0:
			queue.append((d, answer + 'D'))
			visited[d] = 1
		if visited[s] == 0:
			queue.append((s, answer + 'S'))
			visited[s] = 1
		if visited[l] == 0:
			queue.append((l, answer + 'L'))
			visited[l] = 1
		if visited[r] == 0:
			queue.append((r, answer + 'R'))
			visited[r] = 1

t = int(input())

for _ in range(t):
	start, target = map(int, input().split())
	print(bfs(start, target))
