import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

v, e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, v + 1):
    print("INF" if distance[i] == INF else distance[i])
