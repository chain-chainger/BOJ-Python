import sys
input = sys.stdin.readline

def dfs(current):
    global answer
    if current == n:
        count = 0
        for i in range(n):
            if eggs[i][s] <= 0:
                count += 1
        answer = max(answer, count)
        return
    if eggs[current][s] <= 0:
        dfs(current + 1)
        return
    check = True
    for target in range(n):
        if current == target:
            continue
        if eggs[target][s] > 0:
            check = False
            break
    if check:
        answer = max(answer, n - 1)
        return
    for target in range(n):
        if current == target:
            continue
        if eggs[target][s] > 0:
            eggs[target][s] -= eggs[current][w]
            eggs[current][s] -= eggs[target][w]
            dfs(current + 1)
            eggs[target][s] += eggs[current][w]
            eggs[current][s] += eggs[target][w]
            
n = int(input())
s, w = 0, 1
eggs = [list(map(int, input().split())) for _ in range (n)]
answer = 0
dfs(0)
print(answer)