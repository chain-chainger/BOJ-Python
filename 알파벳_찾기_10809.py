import sys
input = sys.stdin.readline

S = input().rstrip()
for c in "abcdefghijklmnopqrstuvwxyz":
    print(S.find(c), end=' ')