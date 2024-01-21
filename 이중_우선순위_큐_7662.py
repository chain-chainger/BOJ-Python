import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    visited = [0] * k
    min_heap, max_heap = [], []
    
    for key in range(k):
        oper, value = input().rstrip().split()
        
        if oper == 'I':
            visited[key] = 1
            heapq.heappush(min_heap, (int(value), key))
            heapq.heappush(max_heap, (-int(value), key))
        else:
            if value == '1':
                while max_heap:
                    target_value, target_key = heapq.heappop(max_heap)
                    if visited[target_key] == 1:
                        visited[target_key] = 0
                        break
            else:
                while min_heap:
                    target_value, target_key = heapq.heappop(min_heap)
                    if visited[target_key] == 1:
                        visited[target_key] = 0
                        break
    
    final_queue = []
    while max_heap:
        target_value, target_key = heapq.heappop(max_heap)
        if visited[target_key] == 1:
            visited[target_key] = 0
            final_queue.append(-target_value)
    while min_heap:
        target_value, target_key = heapq.heappop(min_heap)
        if visited[target_key] == 1:
            visited[target_key] = 0
            final_queue.append(target_value)
            
    if len(final_queue):
        print(max(final_queue), min(final_queue))
    else:
        print("EMPTY")