import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0
    dp[i][1] = i
for i in range(4, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % 1000000003
print(dp[n][k])
