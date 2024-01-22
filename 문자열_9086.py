import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	line = input().rstrip()
	print(f"{line[0]}{line[-1]}")
