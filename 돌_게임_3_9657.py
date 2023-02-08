import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1], dp[3], dp[4] = 1, 1, 1
for i in range(5, n + 1):
	if not dp[i-1] or not dp[i-3] or not dp[i-4]:
		dp[i] = 1
if dp[n]:
	print("SK")
else:
	print("CY")
