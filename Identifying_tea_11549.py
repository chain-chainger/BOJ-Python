import sys
input = sys.stdin.readline

t = int(input())
integers = list(map(int, input().split()))
print(integers.count(t))