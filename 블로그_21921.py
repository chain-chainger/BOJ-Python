import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visits = list(map(int, input().split()))

total = sum(visits[:X])
answer = total
count = 1
for i in range(X, N):
    total += visits[i]
    total -= visits[i - X]
    if total > answer:
        answer = total
        count = 1
    elif total == answer:
        count += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(count)