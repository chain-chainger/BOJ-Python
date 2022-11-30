def bfs(y, x):
    queue = [(y, x)]
    arr[y][x] = 0
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[ny][nx] == 1:
                queue.append((ny, nx))
                arr[ny][nx] = 0
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)