import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
circle = deque([i for i in range(1, N + 1)])
josephus_permutation = []

print("<", end='')
while True:
	circle.rotate(-(K - 1))
	print(circle.popleft(), end='')
	
	if not circle:
		print(">")
		break
	else:
		print(",", end=' ')
