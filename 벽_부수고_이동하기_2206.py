from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c, flag):
    queue = deque()
    queue.append((r, c, flag))
    while queue:
        r, c, flag = queue.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][flag]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if map[nr][nc] == 1 and flag == 0:
                visited[nr][nc][1] = visited[r][c][0] + 1
                queue.append((nr, nc, 1))
            elif map[nr][nc] == 0 and visited[nr][nc][flag] == 0:
                visited[nr][nc][flag] = visited[r][c][flag] + 1
                queue.append((nr, nc, flag))
    return -1

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
n, m = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(bfs(0, 0, 0))
