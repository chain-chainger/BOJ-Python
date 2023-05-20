import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(max_heap, -num)
    else:
        try:
            print(-heapq.heappop(max_heap))
        except:
            print(0)