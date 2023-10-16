import sys
input = sys.stdin.readline

A, B = input().rstrip().split()
A = int(A[::-1])
B = int(B[::-1])
print(max(A, B))