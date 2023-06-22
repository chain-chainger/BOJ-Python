import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
answer = a - b
if answer:
    print(len(answer))
    print(*sorted(list(answer)))
else:
    print(0)