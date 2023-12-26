from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0
queue = deque()
queue.append([N, [N]])

while queue:
    x, move = queue.popleft()
    
    if x == K:
        print(visited[x])
        print(*move)
        break
    
    if 0 <= x - 1 < 100001 and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        temp_move = move + [x - 1]
        queue.append([x - 1, temp_move])
    if 0 <= x + 1 < 100001 and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        temp_move = move + [x + 1]
        queue.append([x + 1, temp_move])
    if 0 <= x * 2 < 100001 and visited[x * 2] == -1:
        visited[x * 2] = visited[x] + 1
        temp_move = move + [x * 2]
        queue.append([x * 2, temp_move])