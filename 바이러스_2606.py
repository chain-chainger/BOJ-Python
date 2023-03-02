from collections import deque
import sys
input = sys.stdin.readline

def bfs(index):
    count = 0
    queue = deque()
    queue.append(index)
    while queue:
        index = queue.popleft()
        for i in network[index]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                count += 1
    return(count - 1)

n = int(input())
m = int(input())
network = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
print(bfs(1))