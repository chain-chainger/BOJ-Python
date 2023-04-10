from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while (queue):
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if tomatoes[nr][nc] == 0:
                tomatoes[nr][nc] = tomatoes[r][c] + 1
                queue.append([nr, nc])

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for r in range(n):
    for c in range(m):
        if tomatoes[r][c] == 1:
            queue.append([r, c])
bfs()
max_day = 0
for r in range(n):
    if 0 in tomatoes[r]:
        print(-1)
        exit(0)
    max_day = max(max_day, max(tomatoes[r]))
print(max_day - 1)