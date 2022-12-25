n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
for i in range(1, k + 1):
    count = []
    for coin in coins:
        if coin <= i and dp[i-coin] != -1:
            count.append(dp[i-coin])
    if count:
        dp[i] = min(count) + 1
    else:
        dp[i] = -1
    print(i, dp[i])
print(dp[k])