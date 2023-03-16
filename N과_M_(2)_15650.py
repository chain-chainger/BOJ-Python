import sys
input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n + 1):
        if i in s:
            continue
        s.append(i)
        dfs(i + 1)
        s.pop()

n, m = map(int, input().split())
s = []
dfs(1)