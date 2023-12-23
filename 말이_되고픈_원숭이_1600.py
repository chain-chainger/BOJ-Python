import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        r, c, count = queue.popleft()
        
        if r == H - 1 and c == W - 1:
            return visited[r][c][count] - 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= H or nc < 0 or nc >= W:
                continue
            if board[nr][nc] == 0 and visited[nr][nc][count] == 0:
                queue.append([nr, nc, count])
                visited[nr][nc][count] = visited[r][c][count] + 1
                
        if count < K:
            for i in range(4, 12):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= H or nc < 0 or nc >= W:
                    continue
                if board[nr][nc] == 0 and visited[nr][nc][count + 1] == 0:
                    queue.append([nr, nc, count + 1])
                    visited[nr][nc][count + 1] = visited[r][c][count] + 1

    return -1

dr = [1, -1, 0, 0, 2, 2, -2, -2, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1, 2, -2, 2, -2]

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

print(bfs())
