import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    queue = deque([(len(a), len(b), len(c))])
    visited = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    while queue:
        a_count, b_count, c_count = queue.popleft()
        if a_count == b_count == c_count == 0:
            return True
        
        if a_count > 0 and a[a_count - 1] == c[c_count - 1] and visited[a_count - 1][b_count] == 0:
            visited[a_count - 1][b_count] = 1
            queue.append([a_count - 1, b_count, c_count - 1])
        if b_count > 0 and b[b_count - 1] == c[c_count - 1] and visited[a_count][b_count - 1] == 0:
            visited[a_count][b_count - 1] = 1
            queue.append([a_count, b_count - 1, c_count - 1])

    return False
            
n = int(input())

for i in range(1, n + 1):    
    first, second, third = input().rstrip().split()
    
    if bfs(first, second, third):
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")