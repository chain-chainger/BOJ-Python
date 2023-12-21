import sys
from collections import deque
input = sys.stdin.readline

def bfs_islands(row, col):
    queue = deque()
    queue.append([row, col])
    islands[row][col] = count
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc] == 1 and islands[nr][nc] == 0:
                queue.append([nr, nc])
                islands[nr][nc] = count

def bfs_answer(island):
    distance = [[0] * N for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(N):
            if islands[i][j] == island:
                queue.append([i, j])
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if islands[nr][nc] != island and islands[nr][nc] != 0:
                return distance[r][c]
            elif islands[nr][nc] == 0 and distance[nr][nc] == 0:
                queue.append([nr, nc])
                distance[nr][nc] = distance[r][c] + 1
    return sys.maxsize
                
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
islands = [[0] * N for _ in range(N)]
answer = sys.maxsize
count = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and islands[i][j] == 0:
            bfs_islands(i, j)
            count += 1

for i in range(1, count - 1):
    answer = min(answer, bfs_answer(i))
print(answer)