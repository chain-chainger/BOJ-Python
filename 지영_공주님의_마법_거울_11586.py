import sys
input = sys.stdin.readline

n = int(input())
original = []
for i in range(n):
    original.append(input().rstrip())
k = int(input())
if k == 2:
    for i in range(n):
        original[i] = original[i][::-1]
elif k == 3:
    original = original[::-1]
for i in range(n):
    print(original[i])
