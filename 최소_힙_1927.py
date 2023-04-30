import heapq
import sys
input = sys.stdin.readline

n = int(input())
min_heap = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(min_heap, num)
    else:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)