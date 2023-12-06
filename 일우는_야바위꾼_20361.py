import sys
input = sys.stdin.readline

N, X, K = map(int, input().split())
cup = [0] * (N + 1)
cup[X] = 1
for _ in range(K):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]
print(cup.index(1))