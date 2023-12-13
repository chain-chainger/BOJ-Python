import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    queue = deque([(row, col)])
    visited[row][col] = 1
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if picture[nr][nc] == picture[r][c] and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
    
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
picture = [input().rstrip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count += 1
print(count, end=' ')

visited = [[0] * N for _ in range(N)]
count = 0

for i in range(N):
    picture[i] = picture[i].replace('R', 'G',)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count += 1
print(count)