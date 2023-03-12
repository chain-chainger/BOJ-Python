import sys
input = sys.stdin.readline

def dfs(x, y, d):
    global count
    if map[x][y] == 0:
        map[x][y] = 2
        count += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if map[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if map[nx][ny] == 1:
        return
    dfs(nx, ny, d)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
count = 0
dfs(r, c, d)
print(count)