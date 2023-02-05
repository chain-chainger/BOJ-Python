import sys
input = sys.stdin.readline

cipher = list(map(int, input().rstrip()))
print(cipher)
dp = [0] * (len(cipher) + 1)
dp[0], dp[1] = 1, 1
if cipher[0] == 0:
    print(0)
    sys.exit()
for i in range(2, len(cipher) + 1):
    if cipher[i-1] > 0:
        dp[i] = dp[i-1]
    if 10 <= (cipher[i-2] * 10) + cipher[i-1] <= 26:
        dp[i] += dp[i-2]
print(dp[-1] % 1000000)
