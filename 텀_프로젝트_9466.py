import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(index):
    global count
    visited[index] = 1
    cycle.append(index)
    if visited[arr[index]] == 1:
        if arr[index] in cycle:
            count -= len(cycle[cycle.index(arr[index]):])
        return
    else:
        dfs(arr[index])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    count = n
    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    print(count)
