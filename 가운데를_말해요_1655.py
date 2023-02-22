import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_h, max_h = [], []
for i in range(n):
    num = int(input())
    if i & 1:
        heapq.heappush(min_h, num)
    else:
        heapq.heappush(max_h, -num)
    if i > 0 and -max_h[0] > min_h[0]:
        max_value = -heapq.heappop(max_h)
        min_value = heapq.heappop(min_h)
        heapq.heappush(max_h, -min_value)
        heapq.heappush(min_h, max_value)
    print(-max_h[0])
