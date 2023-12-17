import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    if row == end_row and col == end_col:
        return 0
    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == end_row and nc == end_col:
                return visited[r][c]
            if nr < 0 or nr >= l or nc < 0 or nc >= l:
                continue
            if visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1           

dr = [2, 2, -2, -2, 1, -1, 1, -1]
dc = [1, -1, 1, -1, 2, 2, -2, -2]
t = int(input())
for _ in range(t):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())
    print(bfs(start_row, start_col))
