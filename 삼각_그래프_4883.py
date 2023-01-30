import sys
input = sys.stdin.readline

k = 0
while True:
    n = int(input())
    if (not n):
        break
    k += 1
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    dp[1][0] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[1][1] + min(graph[0][1], graph[0][1] + graph[0][2], dp[1][0])
    dp[1][2] = graph[1][2] + min(graph[0][1], graph[0][1] + graph[0][2], dp[1][1])
    for i in range(2, n):
        dp[i][0] = graph[i][0] + min(dp[i-1][0], dp[i-1][1])
        dp[i][1] = graph[i][1] + min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2] = graph[i][2] + min(dp[i-1][1], dp[i-1][2], dp[i][1])
    print(f"{k}. {dp[n-1][1]}")
