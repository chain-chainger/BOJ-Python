import sys
input = sys.stdin.readline

def dfs(start):
    prev = 0
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(len(n_list)):
        if i <= start or prev == n_list[i]:
            continue
        prev = n_list[i]
        sequence.append(n_list[i])
        dfs(i)
        sequence.pop()

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
sequence = []
dfs(-1)
