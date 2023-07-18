import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
answer = []
count = 0
for i in range(n):
    team = list(map(int, input().split())) 
    isPass = True
    for i in team:
        if i < l:
            isPass = False
            break
    if isPass:
        if sum(team) >= k:
            answer.extend(team)
            count += 1
print(count)
print(*answer)
