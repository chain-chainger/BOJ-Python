from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        index = queue.popleft()
        for i in relationship[index]:
            if check[i] == 0:
                check[i] = check[index] + 1
                queue.append(i)
            if i == b:
                return

n = int(input())
relationship = [[] for _ in range(n + 1)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)
check = [0] * (n + 1)
bfs(a)
print(check[b] if check[b] > 0 else -1)
