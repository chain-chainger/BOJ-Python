import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    queue = deque([(row, col)])
    answer[row][col] = 0
        
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if board[nr][nc] == 1 and answer[nr][nc] == -1:
                queue.append([nr, nc])
                answer[nr][nc] = answer[r][c] + 1
        

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer[i][j] = 0
        elif board[i][j] == 2:
            bfs(i, j)

for line in answer:
    print(*line)