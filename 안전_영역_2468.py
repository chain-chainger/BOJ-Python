from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and map[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max = 1
for height in range(1, 100):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if map[i][j] > height and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                bfs(i, j)
    if count > max:
        max = count
print(max)