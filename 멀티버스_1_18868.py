import sys
input = sys.stdin.readline

m, n = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    sorted_universe = sorted(universes[i])
    temp = []
    for target in universes[i]:
        temp.append(sorted_universe.index(target))
    universes[i] = temp
answer = 0
for i in range(m - 1):
    for j in range(i + 1, m):
        if universes[i] == universes[j]:
            answer += 1
print(answer)
