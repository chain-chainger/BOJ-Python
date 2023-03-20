import sys
input = sys.stdin.readline

def dfs():
    if len(sequence) == m:
        print(*sequence)
        return
    for number in n_list:
        sequence.append(number)
        dfs()
        sequence.pop()

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
sequence = []
dfs()
