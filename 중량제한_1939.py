from collections import deque
import sys
input = sys.stdin.readline

def bfs(weight):
    queue = deque([island_0])
    visited = [0] * (N + 1)
    visited[island_0] = 1
    
    while queue:
        a = queue.popleft()
        for b, c in bridges[a]:
            if visited[b] == 0 and c >= weight:
                visited[b] = 1
                queue.append(b)
                
    if visited[island_1] == 1:
        return True
    else:
        return False

N, M = map(int, input().split())
bridges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])
island_0, island_1 = map(int, input().split())

start = 1
end = 1000000000
answer = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)