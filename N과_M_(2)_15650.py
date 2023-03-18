import sys
input = sys.stdin.readline

def dfs(start):
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(start, n + 1):
        if i in sequence:
            continue
        sequence.append(i)
        dfs(i + 1)
        sequence.pop()

n, m = map(int, input().split())
sequence = []
dfs(1)