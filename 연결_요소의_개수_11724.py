import sys
from collections import deque
input = sys.stdin.readline

def bfs(index):
    queue = deque([index])
    visited[index] = 1
    
    while queue:
        current = queue.popleft()
        
        for element in linked_elements[current]:
            if visited[element] == 0:
                queue.append(element)
                visited[element] = 1

n, m = map(int, input().split())
linked_elements = [list() for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    linked_elements[u].append(v)
    linked_elements[v].append(u)

visited = [0] * (n + 1)
answer = 0

for i in range(1, n + 1):
    if visited[i] == 0:
        bfs(i)
        answer += 1
        
print(answer)