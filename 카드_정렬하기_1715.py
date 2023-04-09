import heapq
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit(0)
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))
answer = 0
for _ in range(n - 1):
    temp1 = heapq.heappop(cards)
    temp2 = heapq.heappop(cards)
    answer += temp1 + temp2
    heapq.heappush(cards, temp1 + temp2)
print(answer)