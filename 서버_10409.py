import sys
input = sys.stdin.readline

n, t = map(int, input().split())
datas = list(map(int, input().split()))
answer = 0
for data in datas:
    t -= data
    if t >= 0:
        answer += 1
    else:
        break
print(answer)
    