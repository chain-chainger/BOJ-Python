import sys
input = sys.stdin.readline

dp = [0, 1, 2, 3, 5]
n = int(input())
for i in range(5, n + 1):
    dp.append((dp[i-1] + dp[i-2]) % 15746)
print(dp[n])

    
