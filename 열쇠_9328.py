import sys
from collections import deque
input = sys.stdin.readline

def bfs(keys):
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    answer = 0

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr < 0 or nr >= h or nc < 0 or nc >= w or visited[nr][nc] == 1 or building[nr][nc] == '*':
                continue
            
            if building[nr][nc].islower() and visited[nr][nc] == 0:
                key = building[nr][nc].upper()
                keys += key
                if key in doors:
                    for r, c in doors[key]:
                        for i in range(4):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            
                            if nr < 0 or nr >= h + 2 or nc < 0 or nc >= w + 2:
                                continue
                            
                            if visited[nr][nc] == 1:
                                queue.append((r, c))
                                visited[r][c] = 1
                                break
            elif building[nr][nc].isupper() and visited[nr][nc] == 0 and building[nr][nc] not in keys:
                continue
            elif building[nr][nc] == '$' and visited[nr][nc] == 0:
                answer += 1
                
            queue.append((nr, nc))
            visited[nr][nc] = 1
                    
    return answer

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    building = ['.' + input().rstrip() + '.' for _ in range(h)]
    building = ['.' * (w + 2)] + building + ['.' * (w + 2)]
    keys = input().rstrip().upper()
    doors = {}
    
    for i in range(h + 2):
        for j in range(w + 2):
            if building[i][j].isupper():
                if building[i][j] in doors:
                    doors[building[i][j]].append([i, j])
                else:
                    doors[building[i][j]] = list([[i, j]])
                    
    print(bfs(keys))