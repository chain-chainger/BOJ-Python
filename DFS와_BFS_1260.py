from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in graph[start]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for item in graph:
    item.sort() 
visited = [0] * (n + 1)
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)
