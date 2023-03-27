from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr):
    visited = [[1] * 5 for _ in range(5)]
    for i in arr:
        visited[i[0]][i[1]] = 0
    queue = deque([arr[0]])
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                check += 1
                queue.append((nr, nc))
    if check == 7:
        return True
    else:
        return False
                
def dfs(depth, start, count):
    global result
    if count >= 4:
        return
    if depth == 7:
        if bfs(arr):
            result += 1
        return
    for i in range(start, 25):
        r = i // 5
        c = i % 5
        arr.append((r, c))
        dfs(depth + 1, i + 1, count + (students[r][c] == 'Y'))
        arr.pop()    
    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
students = [list(input()) for _ in range(5)]
arr = []
result = 0
dfs(0, 0, 0)
print(result)
