import sys
input = sys.stdin.readline

def dfs(index):
    if len(sequence) == 6:
        print(*sequence)
        return
    for i in range(index, k):
        sequence.append(s[i])
        dfs(i + 1)
        sequence.pop()

while True:
    temp = list(map(int, input().split()))
    k = temp[0]
    if k == 0:
        break
    s = temp[1:]
    sequence = []
    dfs(0)
    print()
    