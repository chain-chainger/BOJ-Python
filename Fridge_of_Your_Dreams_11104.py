import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
	string = input()
	print(int(string, 2))
