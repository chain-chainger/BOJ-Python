import heapq
import sys
input = sys.stdin.readline

n = int(input())
abs_heap = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(abs_heap)[1])
        except:
            print(0)