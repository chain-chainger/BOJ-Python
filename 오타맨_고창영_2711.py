import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	position, string = input().rstrip().split()
	print(string[:int(position) - 1] + string[int(position):])
