import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
if (max(scores) == scores[0]):
    print("S")
else:
    print("N")