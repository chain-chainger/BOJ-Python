import sys
input = sys.stdin.readline

def dfs():
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(1, n + 1):
        sequence.append(i)
        dfs()
        sequence.pop()

n, m = map(int, input().split())
sequence = []
dfs()
