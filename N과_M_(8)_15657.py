import sys
input = sys.stdin.readline

def dfs(start):
    if len(sequence) == m:
        print(*sequence)
        return
    for number in n_list:
        if number < start:
            continue
        sequence.append(number)
        dfs(number)
        sequence.pop()

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
sequence = []
dfs(n_list[0])
