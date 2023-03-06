from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                if nx == k:
                    return visited[nx]
                queue.append(nx)

MAX = 10 ** 5
n, k = map(int, input().split())
visited = [0] * (MAX + 1)
if n == k:
    print(0)
else:
    print(bfs())
