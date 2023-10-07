from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
positions = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])
count = 0
for position in positions:
	while True:
		if dq[0] == position:
			dq.popleft()
			break
		else:
			if dq.index(position) <= len(dq) // 2:
				while dq[0] != position:
					dq.rotate(-1)
					count += 1
			else:
				while dq[0] != position:
					dq.rotate(1)
					count += 1
print(count)
