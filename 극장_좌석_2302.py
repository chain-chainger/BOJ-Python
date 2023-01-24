import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
result = 1
if m > 0:
    pre_vip = 0
    for i in range(m):
        result *= dp[vips[i] - 1 - pre_vip]
        pre_vip = vips[i]
    result *= dp[n-pre_vip]
else:
    result = dp[n]
print(result)