from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        cur_x, cur_y = queue.popleft()
        if abs(end_x - cur_x) + abs(end_y - cur_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if visited[i] == 0:
                nx, ny = stores[i][0], stores[i][1]
                if abs(nx - cur_x) + abs(ny - cur_y) <= 1000:
                    queue.append((nx, ny))
                    visited[i] = 1
    print("sad")

t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int, input().split())
    visited = [0] * n
    bfs(start_x, start_y)