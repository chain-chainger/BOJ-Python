import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
queue = deque()
queue.append((a, 1))

while queue:
    number, count = queue.popleft()
    
    if number == b:
        print(count)
        exit()
    
    if number * 2 <= b:
        queue.append((number * 2, count + 1))
        
    if number * 10 + 1 <= b:
        queue.append((number * 10 + 1, count + 1))
        
print(-1)