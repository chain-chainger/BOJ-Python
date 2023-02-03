import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for len in range(n):
    for start in range(n - len):
        end = start + len
        if start == end:
            dp[start][end] = 1
        elif sequence[start] == sequence[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])