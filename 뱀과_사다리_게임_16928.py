import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	visited = [0] * 101
	queue = deque()
	queue.append((1, 0))
	visited[1] = 1

	while queue:
		current, count = queue.popleft()

		if current == 100:
			return count
		
		for i in range(1, 7):
			next = current + i

			if next in link_info:
				next = link_info[next]
			
			if next < 101 and visited[next] == 0:
				queue.append((next, count + 1))
				visited[next] = 1

n, m = map(int, input().split())
link_info = {}
for _ in range(n + m):
	start, destination = map(int, input().rstrip().split())
	link_info[start] = destination

print(bfs())

