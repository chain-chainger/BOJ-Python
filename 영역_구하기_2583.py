import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    global count
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= m or nc >= n:
            continue
        if matrix[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            count += 1
            dfs(nr, nc)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
m, n, k = map(int, input().split())
rectangles = [list(map(int, input().split())) for _ in range(k)]
matrix = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
counts = []
for i in range(k):
    for r in range(rectangles[i][1], rectangles[i][3]):
        for c in range(rectangles[i][0], rectangles[i][2]):
            matrix[r][c] = 1
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            count = 1
            dfs(i, j)
            counts.append(count)
counts.sort()
print(len(counts))
print(*counts)