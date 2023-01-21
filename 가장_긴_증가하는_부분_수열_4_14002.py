import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
max_dp = max(dp)
res = []
for i in range(n -1, -1, -1):
    if max_dp == dp[i]:
        res.append(a[i])
        max_dp -= 1
res.reverse()
print(*res)