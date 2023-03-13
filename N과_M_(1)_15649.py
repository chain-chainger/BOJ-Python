import sys
input = sys.stdin.readline

def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

n, m = map(int, input().split())
s = []
dfs()
