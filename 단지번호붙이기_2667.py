from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    map[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if map[nx][ny] == 1:
                queue.append((nx, ny))
                map[nx][ny] = 0
                count += 1
    return count

n = int(input().rstrip())
map = [list(map(int, input().rstrip())) for _ in range (n)]
counts = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            counts.append(bfs(i, j))
counts.sort()
print(len(counts))
for count in counts:
    print(count)