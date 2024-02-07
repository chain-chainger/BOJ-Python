import sys
input = sys.stdin.readline

n, m = map(int, input().split())
impossible = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if party & impossible:
            impossible.update(party)

answer = 0
for party in parties:
    if party & impossible:
        continue
    answer += 1

print(answer)
